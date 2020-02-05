import cv2
import numpy as np
from math import *
import imutils

img = cv2.imread(input("name: ")+".jpg")
img = imutils.resize(img, 450)
font = cv2.FONT_HERSHEY_SIMPLEX

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0, 33, 63])
upper = np.array([26, 183, 255])

mask = cv2.inRange(hsv_img, lower, upper)

mask = cv2.dilate(mask, None, iterations=3)
mask = cv2.erode(mask, None, iterations=3)

cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[0] # extra job
# or we cann use
# max_cnts = max(cnts, key=cv2.contourArea)

ep = .003 * cv2.arcLength(max_cnts, True)
max_cnts = cv2.approxPolyDP(max_cnts, ep, True)

out_hall = cv2.convexHull(max_cnts, returnPoints=False) # returns the indexes instead of points if returnPoints is False

defects = cv2.convexityDefects(max_cnts, out_hall)


n = 1

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(max_cnts[s, 0])
    end = tuple(max_cnts[e, 0])
    far = tuple(max_cnts[f, 0])

    d_se = hypot(start[0] - end[0], start[1] - end[1])
    d_sf = hypot(start[0] - far[0], start[1] - far[1])
    d_fe = hypot(far[0] - end[0], far[1] - end[1])

    angle = degrees( acos( (d_sf**2 + d_fe**2 - d_se**2) / (2 * d_sf * d_fe) ) )

    if angle <= 90:
        n += 1

cv2.drawContours(img, [max_cnts], -1, (0, 255, 0), 3)
#cv2.drawContours(img, [out_hall], -1, (0, 255, 0), 3)
cv2.putText(img, f"Number: {n}", (20, 20), font, 0.5, (0, 255, 0), 2)

cv2.imshow("star", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
