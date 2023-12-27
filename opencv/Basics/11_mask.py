# Create_masking

import numpy as np 
import argparse
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())


image = cv2.imread(args['image'])
image = cv2.resize(image, (500,300))
cv2.imshow("Original", image)
# cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Mask", mask)

cv2.rectangle(img = mask, pt1 = (0, 0), pt2 = (300, 200), color = 255, thickness = -1)
cv2.imshow("Mask_rectange", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to image", masked)
cv2.waitKey(0)