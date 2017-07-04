import cv2
import time
import numpy as np


bike_classifier = cv2.CascadeClassifier('HaarCascade20.xml')


img = cv2.imread('49.jpg',1)

bikes = bike_classifier.detectMultiScale(img,1.5,2)
cv2.imshow('bikes',img)
while(1):
    for (x,y,w,h) in bikes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('bikes',img)
    if cv2.waitKey(1) == 27:
        break



cv2.destroyAllWindows()
