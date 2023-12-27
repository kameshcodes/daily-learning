import numpy as np 
import cv2


canvas = np.zeros((300, 300, 3), dtype = "uint8")

# BGR order
green = (0, 255, 0)
cv2.line(canvas, pt1 = (0,0), pt2 = (300,300), color = green, thickness=2)
cv2.imshow("Canvas", canvas) 
cv2.waitKey(0)

green = (0, 0, 255)
cv2.line(canvas, pt1 = (300,0), pt2 = (0,300), color = green, thickness=5)
cv2.imshow("Canvas", canvas) 
cv2.waitKey(0)


green = (0, 255, 0)
cv2.rectangle(canvas, pt1 = (10,10), pt2 = (60,60), color = green, thickness=2)
cv2.imshow("Canvas", canvas) 
cv2.waitKey(0)

cv2.circle(canvas, center=(150,150), radius=50, color=green, thickness=-1)
cv2.imshow("Canvas", canvas) 
cv2.waitKey(0)