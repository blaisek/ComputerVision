import cv2
import numpy as np


#vc = cv2.VideoCapture("http://admin:cam6353@10.10.7.205/video2.mjpg")
vc = cv2.VideoCapture("bikes1.avi")
while (vc.isOpened() == 1):

    ret,frame = vc.read()
    cv2.imshow("fluxIp",frame)
    canny = cv2.Canny(frame,50,120)
    cv2.imshow("canny",canny)

    key = cv2.waitKey(1)
    if key == 27:
        break

vc.release()
cv2.destroyAllWindows()
