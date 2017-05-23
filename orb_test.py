import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('drink.jpg',0)
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
cv2.imshow('drink',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
