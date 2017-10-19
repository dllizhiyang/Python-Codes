
# import the necessary packages
import cv2

# load the video
camera = cv2.VideoCapture('E:\Dropbox\Python Codes\onGitHub\Image Processing, targeting, and recognition\LabDemo.mp4')
#camera = cv2.VideoCapture('D:\Dropbox\Python Codes\onGitHub\Image Processing, targeting, and recognition\LabDemo.mp4')


# keep looping
while True:
	# grab the current frame and initialize the status text
	(grabbed, frame) = camera.read()
	status = "No Targets"

	# check to see if we have reached the end of the
	# video
	if not grabbed:
		break

	# convert the frame to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (7, 7), 0)
	edged = cv2.Canny(blurred, 50, 150)

	# find contours in the edge map
	image, contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	# loop over the contours
	for i in contours:
		# approximate the contour
		epsilon  = cv2.arcLength(i, True) #calculate the length of contour
		approx = cv2.approxPolyDP(i, 0.01 * epsilon, True) # make it a polygon which close to the origional shape(0.01% error)
		# There will be lots of polygon found, we need to find the rectangular, which has only 4~5 vertex coordnate
		# print(approx)

		# ensure that the approximated contour is "roughly" rectangular
		if len(approx) >= 4 and len(approx) <= 5:
			# compute the bounding box of the approximated contour and use the bounding box to compute the aspect ratio
			#print(approx)
			(x, y, w, h) = cv2.boundingRect(approx)
			aspectRatio = w / float(h)
			#print(aspectRatio)

			# compute the solidity of the original contour
			area = cv2.contourArea(i)
			hullArea = cv2.contourArea(cv2.convexHull(i))
			solidity = area / float(hullArea)

			# compute whether or not the width and height, solidity, and aspect ratio of the contour falls within appropriate bounds
			keepDims = w > 25 and h > 25
			keepSolidity = solidity > 0.9
			keepAspectRatio = aspectRatio >= 0.8 and aspectRatio <= 1.9


			# ensure that the contour passes all our tests
			if keepDims and keepSolidity and keepAspectRatio:
				# draw an outline around the target and update the status texts
				#print(approx)
				cv2.drawContours(frame, [approx], -1, (0, 255, 0), 4)
				status = "Target(s) Acquired"

				# compute the center of the contour region and draw the crosshairs
				M = cv2.moments(approx)
				(cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
				(startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
				(startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
				cv2.line(frame, (startX, cY), (endX, cY), (0, 255, 0), 3)
				cv2.line(frame, (cX, startY), (cX, endY), (0, 255, 0), 3)
				cv2.putText(frame, "Center(%s,%s), Confidence(%s)"% (str(cX),str(cY), str(solidity)), (20,700),cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0, 255, 0), 2 )


	# draw the status text on the frame
	#cv2.putText(frame, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255), 2)


	# show the frame and record if a key is pressed
	#########  Main()  ################
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(25) & 0xFF   # waitKey control the playback speed

	if key == ord(" "):
		key = cv2.waitKey(0)

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break


