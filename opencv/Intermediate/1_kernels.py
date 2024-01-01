import numpy as np 
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())


image = cv2.imread(args['image'])
print(image.shape)
image = cv2.resize(image, (500,300))
cv2.imshow("Original", image)
cv2.waitKey(0)


kernelsizes = [(3,3), (9,9), (15,15)]

# Average Blur
for (kX, kY) in kernelsizes:
    blurred_img = cv2.blur(image, (kX, kY))
    cv2.imshow(f"Average ({kX}, {kY})", blurred_img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur
for (kX, kY) in kernelsizes:
    blurred_img = cv2.GaussianBlur(image, (kX,kY), 0) #read parameters of this 
    cv2.imshow(f"Gaussian ({kX}, {kY})", blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# Median Blur 
for k in (3, 9, 15):
    blurred_img = cv2.medianBlur(image, k) 
    cv2.imshow(f"Meadian K {k}", blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()