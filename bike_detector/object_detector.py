#usage
# python object_detector.py --detector bike_detector.svm
# --video bikes1.mp4
# importation des paquets
import dlib
import cv2
import imutils
import argparse
import numpy as np

# arguments du programme
ap = argparse.ArgumentParser()
ap.add_argument("-d","--detector",required = True,
                help="chemin vers le detecteur svm")
ap.add_argument("-v","--video",required = True,
                help = "chemin vers le fichier video")
args = vars(ap.parse_args())

# initialisation des objets
detector = dlib.simple_object_detector(args["detector"])
fourcc = cv2.cv.FOURCC('M','J','P','G')
cap = cv2.VideoCapture(args["video"])
out = None
# lecture des trames
while cap.isOpened():


    ret, frame = cap.read()
    if not ret:
        break
    # redimensionnement des trames
    frame = imutils.resize(frame,width=400)
    #application du detecteur a chaque trames
    det = detector(frame)

    # si objet, dessine rectangle d'encadrement en vert
    for d in det:
        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 255, 0), 2)

    # affichage et touche de sortie
    cv2.imshow("frame",frame)
    if out is None:
     (h,w) = frame.shape[:2]
     out = cv2.VideoWriter("bike5_detector.avi", fourcc, 30, (w, h), True)
     output = np.zeros((h,w,3),dtype="uint8")

    output[0:h,0:w]= frame
    out.write(output)
    cv2.imshow("output",output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#libere les ressources
cap.release()
out.release()
cv2.destroyAllWindows()
