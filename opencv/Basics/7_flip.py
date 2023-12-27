# flip

import numpy as np 
import argparse
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.resize(image, (500, 300))
cv2.imshow("Original", image)


h_flipped = cv2.flip(image, 1) #{1:horizontal, 0: veritical, -1 : both horizontal and vertical}
cv2.imshow("Horizontal Flip", h_flipped)

v_flipped = cv2.flip(image, 0) #{1:horizontal, 0: veritical, -1 : both horizontal and vertical}
cv2.imshow("Vertical Flip", v_flipped)

hv_flipped = cv2.flip(image, -1) #{1:horizontal, 0: veritical, -1 : both horizontal and vertical}
cv2.imshow("Both h and v Flip", hv_flipped)

cv2.waitKey(0)

