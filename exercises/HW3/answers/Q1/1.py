import cv2
import imutils
import numpy as np

name = input("name: ")
img = cv2.imread(name+".jpg")
img = cv2.GaussianBlur(img, (9, 9), 81)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


sob = cv2.Sobel(gray, cv2.CV_8U, dx=1, dy=1, ksize=5)

cnts, _ = cv2.findContours(sob, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.imshow("window", sob)
cv2.waitKey()
