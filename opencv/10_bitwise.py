import numpy as np 
import cv2 

rectangle = np.zeros((300, 300), dtype = 'uint8')
cv2.rectangle(img = rectangle, pt1 = (25,25), pt2 = (275, 275), color=255, thickness=-1)
cv2.imshow("Rectange", rectangle)

#binary image : white or black pixel only
circle = np.zeros((300,300), dtype = "uint8")
cv2.circle(img = circle, center=(150,150), radius=150, color = 255, thickness=-10)
cv2.imshow("Circle", circle)
cv2.waitKey(0)


# a bitwise "And" is true when both pixels are "ON"
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("And", bitwiseAnd)


# a bitwise "And" is true when pixel of either image are "ON"
bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOR)


bitwiseNOT = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNOT)
cv2.waitKey(0)