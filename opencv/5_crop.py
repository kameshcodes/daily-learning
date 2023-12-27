# Cropping

import numpy as np 
import argparse
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.resize(image, (500, 300))

print(image.shape)

cv2.imshow("Original", image)

print(image.shape)
face = image[0:175,200:350]
cv2.imshow("Face", face)
cv2.waitKey(0)