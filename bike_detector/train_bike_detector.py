#USAGE
# python train_bike_detector.py -a bikedataset.xml -o bike_detector.svm
# import des paquets
import os
import sys
import glob
import dlib
import argparse
#from skimage import io

# arguments du programme
ap = argparse.ArgumentParser()
ap.add_argument("-a","--annotations",required = True,
                help="chemin vers le fichier xml")
ap.add_argument("-o","--output",required = True,
                help = "chemin et nom du fichier .svm a creer")
args = vars(ap.parse_args())

#chargement des options
option = dlib.simple_object_detector_training_options()

#pivoter les images a extraire
option.add_left_right_image_flips = True
#fixe la marge de decision 
option.C = 5
#nombre de threads
option.num_threads = 4
#verbeux
option.be_verbose = True
# entrainement du detecteur de cyclistes 
dlib.train_simple_object_detector(args["annotations"],args["output"],option)

