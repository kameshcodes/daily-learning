import numpy as np 
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="photo1.jpg", help = "path to the input image")
args = vars(ap.parse_args())


image = cv2.imread(args['image'])
image = cv2.resize(image, (500,300))



#RGB
cv2.imshow("Original", image)
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)
    
cv2.waitKey(0)
cv2.destroyAllWindows()


#HSV transformation from cube to cylinder
cv2.imshow("Original", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)
cv2.waitKey(0)
cv2.destroyAllWindows()
  
    
cv2.imshow("Original", image)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("lab", lab)

for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
    cv2.imshow(name, chan)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows(0)