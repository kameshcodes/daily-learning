# resize

import numpy as np 
import argparse
import imutils
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

#############################################
resized = imutils.resize(image, width=300, inter=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
#############################################

# Note use imutils ka resize image to resize image.