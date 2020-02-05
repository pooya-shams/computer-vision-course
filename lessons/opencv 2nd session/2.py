""" direct way of getting binary image
colored image -> binary """

import cv2
import numpy as np

img = cv2.imread("ball.png")

lower = np.array([28, 77, 82])
upper = np.array([154, 255, 255])

binary = cv2.inRange(img, lower, upper) # -> (image matrix, lower, upper) --> returns 

cv2.imshow("window", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
