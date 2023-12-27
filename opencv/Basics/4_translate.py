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

#############################################################################
# Translation Matrix is given by the matrix of form:
#   [
#     [1, 0, shiftX],   -ve value shift left
#     [0, 1, shiftY]    -ve value shift up 
#   ]


# Construct a translation matrix M to shift the image 25 pixel right and 50 pixel down
M = np.float32([[1,0,25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted )

# Construct a translation matrix M to shift the image 25 pixel left and 50 pixel up
M = np.float32([[1,0,-25], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted )
cv2.waitKey(0)
################################################################################

shifted = imutils.translate(image, x = 100, y = 50)
cv2.imshow("Shifted Down and Right", shifted )
cv2.waitKey(0)
cv2.destroyAllWindows()