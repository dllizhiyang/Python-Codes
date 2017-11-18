
class select_and_find:

    def Template_Matching_blur_to_blur(self):
        input_img = cv2.imread('%s'%circuit_path,0)
        gauss_blurred_img = cv2.GaussianBlur(input_img, (7, 7), 0)
        image_height = gauss_blurred_img.shape[0]
        image_wide = gauss_blurred_img.shape[1]
        img0 =cv2.imread('%s'%circuit_path)
        img2 = input_img.copy()
        template = cv2.imread('%s_section1_blurred.jpg'%template_path,0)
        template_shown = cv2.imread('%s'%template_path)
        print("%s,%s"%(image_height,image_wide))
        h = template.shape[0]
        w = template.shape[1]

        start = time.time()
        res = cv2.matchTemplate(gauss_blurred_img,template,cv2.TM_CCOEFF_NORMED) ####### matchTemplate Function
        end = time.time()
        processing_time = round((end-start)*1000,2)

        threadhold = 0.9
        loc = np.where(res >= threadhold)
        shown_guass_blurred = cv2.cvtColor(gauss_blurred_img,cv2.COLOR_GRAY2RGB)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        for pt in zip(*loc[::-1]):
            cv2.rectangle(shown_guass_blurred,pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
            cv2.putText(shown_guass_blurred, "Center(%s,%s)"% (str(pt[0]),str(pt[1])),(int(image_wide/10),int(image_height/1.05)),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2 )
            cv2.putText(shown_guass_blurred, "Time: %s ms"% (str(processing_time)),(int(image_wide/1.8),int(image_height/1.05)),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2 )

        b = shown_guass_blurred[:, :, 0]
        g = shown_guass_blurred[:, :, 1]
        r = shown_guass_blurred[:, :, 2]
        shown_guass_blurred = cv2.merge((r, g, b))

        cv2.imshow('marker',template_shown)
        cv2.imshow('Blur-Blur_result',shown_guass_blurred)
        print("%s ms"%(str(processing_time)))
        cv2.waitKey(0)


    def Template_Matching_edge_to_blur(self):
        input_img = cv2.imread('%s'%circuit_path,0)
        gauss_blurred_img = cv2.GaussianBlur(input_img, (7, 7), 0)
        image_height = gauss_blurred_img.shape[0]
        image_wide = gauss_blurred_img.shape[1]
        img0 =cv2.imread('%s'%circuit_path)
        img2 = input_img.copy()
        template = cv2.imread('%s_section1_blurred.jpg'%template_path,0)
        edge_template = cv2.Canny(template,50, 150)
        template_shown = cv2.imread('%s'%template_path)
        print("%s,%s"%(image_height,image_wide))
        h = template.shape[0]
        w = template.shape[1]

        start = time.time()
        res = cv2.matchTemplate(gauss_blurred_img,edge_template,cv2.TM_CCOEFF_NORMED) ####### matchTemplate Function
        end = time.time()
        processing_time = round((end-start)*1000,2)

        threadhold = 0.3
        loc = np.where(res >= threadhold)
        shown_guass_blurred = cv2.cvtColor(gauss_blurred_img,cv2.COLOR_GRAY2RGB)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        for pt in zip(*loc[::-1]):
            cv2.rectangle(shown_guass_blurred,pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
            cv2.putText(shown_guass_blurred, "Center(%s,%s)"% (str(pt[0]),str(pt[1])),(int(image_wide/10),int(image_height/1.05)),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2 )
            cv2.putText(shown_guass_blurred, "Time: %s ms"% (str(processing_time)),(int(image_wide/1.8),int(image_height/1.05)),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2 )

        b = shown_guass_blurred[:, :, 0]
        g = shown_guass_blurred[:, :, 1]
        r = shown_guass_blurred[:, :, 2]
        shown_guass_blurred = cv2.merge((r, g, b))

        cv2.imshow('marker',edge_template)
        cv2.imshow('Edge-Blur_result',shown_guass_blurred)
        print("%s ms"%(str(processing_time)))
        cv2.waitKey(0)


    def Template_Matching_edge_to_edge(self):
        input_img = cv2.imread('%s'%sample_path,0)
        gauss_blurred_img = cv2.GaussianBlur(input_img, (7, 7), 0)
        # Original:edged_img = cv2.Canny(gauss_blurred_img,50, 150)
        edged_img = cv2.Canny(gauss_blurred_img,100, 50)
        image_height = gauss_blurred_img.shape[0]
        image_wide = gauss_blurred_img.shape[1]
        img0 =cv2.imread('%s'%sample_path)
        img2 = input_img.copy()
        template = cv2.imread('%s_edge.png'%template_path,0)
        template_shown = cv2.imread('%s'%template_path)
        print("%s,%s"%(image_height,image_wide))
        h = template.shape[0]
        w = template.shape[1]

        start = time.time()
        #res = cv2.matchTemplate(edged_img,template,cv2.TM_CCOEFF_NORMED) ####### matchTemplate Function
        res = cv2.matchTemplate(edged_img,template,cv2.TM_CCORR_NORMED) ####### matchTemplate Function
        end = time.time()
        processing_time = round((end-start)*1000,2)

        threadhold = 0.45
        loc = np.where(res >= threadhold)
        shown_edged_img = cv2.cvtColor(edged_img,cv2.COLOR_GRAY2RGB)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        for pt in zip(*loc[::-1]):
            print(pt)
            cv2.rectangle(shown_edged_img,pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
            cv2.putText(shown_edged_img, "Center(%s,%s)"% (str(pt[0]),str(pt[1])),(int(image_wide/10),int(image_height/1.05)),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2 )
            cv2.putText(shown_edged_img, "Time: %s ms"% (str(processing_time)),(int(image_wide/1.8),int(image_height/1.05)),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2 )

        b = shown_edged_img[:, :, 0]
        g = shown_edged_img[:, :, 1]
        r = shown_edged_img[:, :, 2]
        shown_edged_img = cv2.merge((r, g, b))

        cv2.imshow('marker',template_shown)
        cv2.imshow('Edge-Edge_result',shown_edged_img)
        print("%s ms"%(str(processing_time)))
        cv2.waitKey(0)

###########################  Figure Select Function() #####################################################

def on_mouse(event, x, y, flags,param):
    global img, point1, point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 2)
        cv2.imshow('Selected Area', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        cv2.rectangle(img2, point1, (x,y), (0,2552,0), 2)
        cv2.imshow('Selected Area', img2)
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (255,0,255), 2)
        cv2.imshow('Selected Area', img2)
        min_x = min(point1[0],point2[0])
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        cut_img = img[min_y:min_y+height, min_x:min_x+width]
        cv2.imwrite('%s'%template_path, cut_img)
        blurred = cv2.GaussianBlur(cut_img, (7, 7), 0)
        cv2.imwrite('%s_blurred.png'%template_path, blurred)
        cv2.imshow("blurred",blurred)
        # Original: edged = cv2.Canny(cut_img, 50, 150)
        edged = cv2.Canny(cut_img, 170, 50)
        cv2.imwrite('%s_edge.png'%template_path,edged)
        cv2.imshow("edge",edged)
        #select_and_find.Template_Matching_blur_to_blur()  ###### start search #############
        demo = select_and_find()
        #demo.Template_Matching_blur_to_blur()
        #demo.Template_Matching_edge_to_blur()
        demo.Template_Matching_edge_to_edge()


########################################  Main () ##############################################
import cv2
import numpy as np
import time

def main():
    global img
    global point1, point2
    global training_path
    global template_path
    global sample_path
    training_path = 'training.png'
    template_path = 'marker_section.png'
    sample_path = 'sample_2.png'
    #circuit_path = 'iphone_pcb.jpg'
    #template_path = 'iphone_pcb_section1.jpg'
    global img
    img = cv2.imread('%s'%training_path)
    print(time.time())
    cv2.namedWindow('Selected Area')
    cv2.setMouseCallback('Selected Area', on_mouse)
    cv2.imshow('Selected Area', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


