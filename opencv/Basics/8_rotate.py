# rotate

import numpy as np 
import argparse
import imutils
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = imutils.resize(image = image, width=500)

cv2.imshow("Original", image)

# In order to rotate the image, we need to define the point around which we are gonna rotate the image.
(h,w) = image.shape[:2]
(cX, cY) = (w//2, h//2)

################################################################
M = cv2.getRotationMatrix2D(center=(cX, cY), angle=45, scale = 1.3)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 counterclockwise", rotated)

M = cv2.getRotationMatrix2D(center=(cX, cY), angle=-45, scale = 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 clockwise", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
################################################################

rotated = imutils.rotate(image, -45)
cv2.imshow("Rotated by 45 clockwise", rotated)
cv2.waitKey(0)


rotated = imutils.rotate_bound(image, -45)
cv2.imshow("Rotated by 45 clockwise with rotatebound", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()


