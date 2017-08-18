import cv2
import numpy as np

img = cv2.imread('drink.jpg',1)
camera = cv2.VideoCapture(0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img,None)
img2 = cv2.drawKeypoints(img, kp1, None, color=(0,255,0), flags=0)

cv2.imshow('drink',img2)

while (camera.isOpened() ==1):

    ret, imgCamColor = camera.read()
    #imgCamGray=cv2.cvtColor(imgCamColor,cv2.COLOR_BGR2GRAY)
    kpCam,descam = orb.detectAndCompute(imgCamColor,None)


    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)

    matches = bf.match(descam,des1)
    matches = sorted(matches,key= lambda val: val.distance)
    cv2.imshow("camera",imgCamGray)
    k = cv2.waitKey(30) & 0xff
    if k == 27: #ESC
        break



camera.release()
cv2.destroyAllWindows()
