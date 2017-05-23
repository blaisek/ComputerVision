import numpy as np  #extension pour la manipulation de matrices
import cv2

cap = cv2.VideoCapture('http://admin:cam6353@10.10.7.205/video2.mjpg')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27: #ESC
        break

cap.release()
cv2.destroyAllWindows()
