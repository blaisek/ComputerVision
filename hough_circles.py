import cv2
import numpy as np


vc = cv2.VideoCapture("http://admin:cam6353@10.10.7.205/video2.mjpg")

while (vc.isOpened() == 1):

    ret,frame = vc.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,5)
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1.5,10)
    #circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.5,10)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(frame,(i[0],i[1]),i[2],(255,0,0),2)
        cv2.circle(frame,(i[0],i[1]),2,(0,255,0),5)

    cv2.imshow("HoughCircles",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

vc.release()
cv2.destroyAllWindows()
