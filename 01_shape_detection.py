import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread("07_Alistirmalar/resimler/polygons.png")
cv2.resize(img,(800,600))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

contours, ret = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon, True) 

    cv2.drawContours(img,[approx],0,(0),5)

    x=approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx)==3:
        cv2.putText(img,"Triangle",(x,y), font , 1, (0))
    
    elif len(approx)==4:
        cv2.putText(img,"Rectangle",(x,y), font , 1, (0))

    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y), font , 1, (0))

    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y), font , 1, (0))

    else:
        cv2.putText(img,"Circle",(x,y), font , 1, (0))


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
