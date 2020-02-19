import cv2
import imutils
import numpy as np
from math import *

font = cv2.FONT_HERSHEY_SIMPLEX

lower = np.array([0, 0, 127])
upper = np.array([255, 255, 255])

def half_sort(lis):
    mi = lis.index(min(lis))
    nl = lis[mi:]+lis[:mi]
    return nl

def unique(lis):
    nl = []
    for i in lis:
        if not i in nl:
            nl.append(i)
    return nl[:]

def angles(img, cnt_index=None, width=None, height=None):
    img = imutils.resize(img, width, height)
    img = cv2.GaussianBlur(img, (3, 3), 6)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.bitwise_not(mask)
    #mask = cv2.erode(mask, None, iterations=2)
    #mask = cv2.dilate(mask, None, iterations=2)
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if cnt_index == None:
        cnt = max(cnts, key=cv2.contourArea)
    else:
        cnt = cnts[cnt_index]
    ep = .003 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, ep, True)

    rect = cv2.minAreaRect(cnt)
    img = imutils.rotate_bound(img, rect[2])
    if rect[1][0] > rect[1][1]:
        img = imutils.rotate_bound(img, -90)


    con_hull = cv2.convexHull(approx, returnPoints=False)
    defects = cv2.convexityDefects(approx, con_hull)
    l = []
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(approx[s, 0])
        end = tuple(approx[e, 0])
        far = tuple(approx[f, 0])

        d_se = hypot(start[0] - end[0], start[1] - end[1])
        d_sf = hypot(start[0] - far[0], start[1] - far[1])
        d_fe = hypot(far[0] - end[0], far[1] - end[1])

        angle = degrees( acos( (d_sf**2 + d_fe**2 - d_se**2) / (2 * d_sf * d_fe) ) )
        l.append(angle)
    l.sort()
    l = unique(l)
    return l


# creating data for comparing later
# data is a list from angles of the numbers
"""
number_angles = list(range(10))
for i in range(10):
    img = cv2.imread(f"numbers\\{i}.png")
    angle = angles(img, height=200)
    number_angles[i] = angle
    print(angle)

"""
print()

shape_angles = []
for i in range(10):
    img = cv2.imread("pic.png")
    angle = angles(img, i, height=100)
    print(angle)
