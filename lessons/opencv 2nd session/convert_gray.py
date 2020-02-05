import cv2
import numpy as np

img = cv2.imread("ball.png")

lower = np.array([28, 77, 82])
upper = np.array([154, 255, 255])

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # converts to hsv (hue saturation value)

bin_img = cv2.inRange(hsv_img, lower, upper) # converts from hsv to binay range

out_img = cv2.bitwise_and(img, img, mask=bin_img) # just returns the important parts (actuall filters the parts that arent in mask)

cv2.imshow("window", out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
