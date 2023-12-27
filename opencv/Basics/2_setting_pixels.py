import numpy as np 
import argparse
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())

image  = cv2.imread(args["image"])  #image is 3 channel array
image = cv2.resize(image, (300, 300))

(b,g,r) =  image[250, 30]
print(f"pixel at (0,0) b: {b}, g: {g}, r: {r}")

image[250, 30] = (0, 0, 255)
(b,g,r) =  image[250, 30]
print(f"pixel at (0,0) b: {b}, g: {g}, r: {r}")