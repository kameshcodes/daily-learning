# image is matrix for opencv

import numpy as np 
import argparse
import cv2

# Consturct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())

# Images are NumPy array stored as unsigned 8-bit integers (uint8)
# With values in the range [0, 255]; when using the add/subtract 
# functions in OpenCv, these values will be *clipped* to this range,
# even if they fall outside the range[0, 255] after applying the operation

print("\nopencv: clipped at max min ")
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print(f"Max of 255: {added}")
print(f"Min of 0: {subtracted}")

print("\nNumpy:")
added = np.add(np.uint8([200]), np.uint8([100]))
subtracted = np.subtract(np.uint8([50]), np.uint8([100]))
print(f"Max of 255: {added}")
print(f"Min of 0: {subtracted}")


# adjusting the brighness of image using image arithmetic

# load input image
image = cv2.imread(args['image'])
image = cv2.resize(image, (500, 300))

cv2.imshow("Original", image)

# increasing the pixel intensities in our image by 100
# construct numpy array that has same dimesion as our input image
# fill it with ones and multiply by 100 and add the input image and matrix togeather
M = np.ones(image.shape, dtype = "uint8")*100
added  = cv2.add(image, M)
cv2.imshow("Lighter", added)

M = np.ones(image.shape, dtype="uint8")*100
sub = cv2.subtract(image, M)
cv2.imshow("Darker", sub)
cv2.waitKey(0)