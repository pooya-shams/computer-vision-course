import cv2
import numpy as np

window_name = "gray filter"

cv2.namedWindow(window_name)

cv2.createTrackbar("Rmin", window_name, 0, 255, lambda x:None)
cv2.createTrackbar("Gmin", window_name, 0, 255, lambda x:None)
cv2.createTrackbar("Bmin", window_name, 0, 255, lambda x:None)
cv2.createTrackbar("Rmax", window_name, 255, 255, lambda x:None)
cv2.createTrackbar("Gmax", window_name, 255, 255, lambda x:None)
cv2.createTrackbar("Bmax", window_name, 255, 255, lambda x:None)

img = cv2.imread("ball.png")

while True:
    rmin = cv2.getTrackbarPos("Rmin", window_name)
    gmin = cv2.getTrackbarPos("Gmin", window_name)
    bmin = cv2.getTrackbarPos("Bmin", window_name)
    rmax = cv2.getTrackbarPos("Rmax", window_name)
    gmax = cv2.getTrackbarPos("Gmax", window_name)
    bmax = cv2.getTrackbarPos("Bmax", window_name)
    mins = np.array([bmin, gmin, rmin])
    maxs = np.array([bmax, gmax, rmax])
    bin_output = cv2.inRange(img, mins, maxs)
    cv2.imshow(window_name, bin_output)
    if cv2.waitKey(30) == ord('q'):
        break
