import numpy as np 
import argparse
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="logo.png", help = "path to the input image")
args = vars(ap.parse_args())

# load the input image and grab each channel
# notide how opencv represents images as NumPy array with channels in "Blue, Green, Red" ordering rather that "RGB ordering"

image  = cv2.imread(args["image"])  #image is 3 channel array
image = cv2.resize(image, (300, 300))
cv2.imshow("Image", image)
(h, w, c) = image.shape[:3]

print("Height: ", h)
print("Width: ", w)
print("Channel: ", c)

# n_row*n_col  [[1,0],
#               [0,0],
#               ]
cv2.waitKey(0)

cv2.imwrite("NewImg.jpg", image)
