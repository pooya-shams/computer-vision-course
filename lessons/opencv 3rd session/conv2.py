import cv2
import numpy as np

img = cv2.imread("rectangle.png")

kernelx = np.array([[-1, 1]])
kernely = np.array([[-1], [1]])

conv_imgx = cv2.filter2D(img, cv2.CV_64F, kernelx)
conv_imgy = cv2.filter2D(img, cv2.CV_64F, kernely)

cv2.imshow("x", conv_imgx)
cv2.imshow("y", conv_imgy)
cv2.waitKey()
cv2.destroyAllWindows()
