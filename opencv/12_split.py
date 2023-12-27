# split and merge channel using openCV library.

import numpy as np 
import argparse
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="logo.png", help = "path to the input image")
args = vars(ap.parse_args())

# load the input image and grab each channel
# notide how opencv represents images as NumPy array with channels in "Blue, Green, Red" ordering rather that "RGB ordering"

image  = cv2.imread(args["image"])
image = cv2.resize(image, (300, 300))
(B, G, R) = cv2.split(image)
# # Note : You split channel to apply arithmetic operations on pixel for eg brightening the red.
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merged = cv2.merge([B, G, R])   # Notice Ordering 

# cv2.imshow("Merged", merged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Viz each channel in color

zeros = np.zeros(image.shape[:2], dtype = 'uint8')
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()
