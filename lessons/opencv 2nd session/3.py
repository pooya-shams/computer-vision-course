""" direct way of getting binary image
colored image(hsv type) -> binary """

import cv2
import numpy as np

img = cv2.imread("ball.png")

lower = np.array([28, 77, 82])
upper = np.array([154, 255, 255])

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # converts to hsv (hue saturation value)

binary = cv2.inRange(hsv_img, lower, upper) # -> (image matrix, lower, upper) --> returns 

cv2.imshow("window", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
