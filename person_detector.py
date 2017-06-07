import cv2
import time
import numpy as np

person_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture('http://admin:cam6353@10.10.7.205/video2.mjpg')


while cap.isOpened():

    #time.sleep(.05)

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    person = person_classifier.detectMultiScale(gray,1.2,2)
    cv2.imshow('gens',frame)
    for (x,y,w,h) in person:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('gens',frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
