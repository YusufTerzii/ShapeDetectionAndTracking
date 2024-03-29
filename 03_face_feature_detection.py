import cv2
import numpy as np

def findMaxContour(contours):
    max_i=0
    max_area = 0

    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])

        if max_area < area_face:
            max_area = area_face
            max_i=i

        try:
            cnt = contours[max_i]

        except:
            contours = [0]
            cnt = contours[0]

        return c


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    roi = frame[50:250, 250:450] ### frame[y1:y2, x1:x2]
    cv2.rectangle(frame,(250,50),(450,250),(0,0,255),0) ##x1,y1 x2,y2

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    lower_color = np.array([0,45,100], np.uint8)
    upper_color = np.array([17,255,255], np.uint8)

    mask = cv2.inRange(hsv,lower_color,upper_color)
    kernel= np.ones((3,3),np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask= cv2.medianBlur(mask,15)

    contours, ret = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours)>0:
        try:
            c = findMaxContour(contours)

            extLeft = tuple(c[c[:,:0].argmin()][0]) ## 0 en küçük x leri bulmak için
            extRight = tuple(c[c[:,:0].argmax()][0])
            extTop = tuple(c[c[:,:1].argmin()][0])

            cv2.circle(roi,extLeft,5,(0,255,0),2)
            cv2.circle(roi,extRight,5,(0,255,0),2)
            cv2.circle(roi,extTop,5,(0,255,0),2)
            

        except:
            pass

        else:
            break
        
        
        
    
    

    





    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break    

cam.release()
cv2.destroyAllWindows()