import cv2
import numpy as np

img = cv2.imread("flowers.png")

kernel = np.ones((3, 3))/9

conv_img = cv2.filter2D(img, cv2.CV_8U, kernel)
blur_img = cv2.blur(img, (7, 7))
conv_img2 = cv2.GaussianBlur(img, (3, 3), 9)

cv2.imshow("conv", conv_img)
cv2.imshow("blur", blur_img)
cv2.imshow("conv2", conv_img2)
cv2.waitKey()
cv2.destroyAllWindows()
