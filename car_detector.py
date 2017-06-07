import cv2
import time
import numpy as np

car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')

cap = cv2.VideoCapture('http://admin:cam6353@10.10.7.205/video2.mjpg')


while cap.isOpened():

    #time.sleep(.05)

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars = car_classifier.detectMultiScale(gray,1.4,2)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('Voitures',frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
