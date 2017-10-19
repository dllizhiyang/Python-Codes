import cv2

class find_Square_Marker:

	def image_preprocess(self,rawImage):
		gray = cv2.cvtColor(rawImage, cv2.COLOR_BGR2GRAY)
		cv2.imshow("gray",gray)
		blurred = cv2.GaussianBlur(gray, (7, 7), 0)
		cv2.imshow('blur',blurred)
		edged = cv2.Canny(blurred, 50, 150)
		cv2.imshow('edged',edged)
		return edged
		#cv2.waitKey(0)

	def image_process_car_plate(self):


	def find_Square(self,rawImage):
		######## Get Processed images ##########
		processed_image = self.image_preprocess(rawImage)  ########## use the method within a class#########

		####### Find the all the countors ###############
		image, contours, hierarchy = cv2.findContours(processed_image.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

		######## Loop each countours to find any rectangule  ##############
		for i in contours:
			epsilon = cv2.arcLength(i,True)
			approx = cv2.approxPolyDP(i,0.05*epsilon,True)
			#print(approx)
			if len(approx)>=4 and len(approx)<=6:  ########  rectangle has roughly 5~6 contours########
				(x,y,w,h) = cv2.boundingRect(approx)
				ratio = w/h
				good_ratio = (ratio>=2 and ratio <= 5)
				#print( "ratio is %s"%ratio)

				############## Calculate the confidence ################
				area = cv2.contourArea(i)
				hullArea = cv2.contourArea(cv2.convexHull(i))
				confidence = area/hullArea
				if confidence>0.9:
					print("Confidence is %s"%confidence)
				if w>25 and h>25 and confidence>0.95 and good_ratio:
					cv2.drawContours(rawImage, [approx], -1, (0, 255, 0), 4)
					cv2.putText(rawImage,"Confidence is %s"%confidence,(x+50,y+200),cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0, 255, 0), 2 )


if __name__ == '__main__':
	imagePath = 'cars\car_04.jpg'
	img = cv2.imread(imagePath)
	example = find_Square_Marker()
	example.find_Square(img)
	cv2.namedWindow('img', cv2.WINDOW_NORMAL)
	cv2.imshow('img', img)
	cv2.waitKey(0)

