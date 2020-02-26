import cv2
import numpy as np
from math import *

font = cv2.FONT_HERSHEY_SIMPLEX
pause = False

lower = np.array([0, 0, 0])
upper = np.array([255, 255, 150])

while True:
    key = cv2.waitKey(30)
    if key == ord('q'):break
    elif key == ord(' '):
        pause = not pause
    if pause:
        continue

    img = cv2.imread("2.png")

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    bin_img = cv2.inRange(hsv_img, lower, upper)

    not_bin_img = cv2.bitwise_not(bin_img)

    cnts, _ = cv2.findContours(not_bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in cnts:
        M = cv2.moments(cnt)
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        ep = 0.03*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, ep, True)
        l = len(approx)
        if l == 3:
            name = "Triangle"
        elif l == 4:
            lengths = []
            for side in range(4):
                lengths.append( hypot(approx[side][0][0] - approx[ (side+1)%4 ][0][0], approx[side][0][1] - approx[ (side+1)%4 ][0][1]) )
            if all(map(lambda x: abs(lengths[0] - x) < 4, lengths )):
                name = "Square"
            else:
                name = "Rectangle"
        elif l == 5:
            name = "Pentagon"
        else:
            name = "Circle"
        mask = np.zeros(img.shape, dtype=np.uint8)
        cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)
        mask = cv2.inRange(mask, (127, 127, 127), (255, 255, 255))
        b, g, r = map(int, cv2.mean(img, mask=mask)[:3])
        color = ""
        if 190 <= b <= 255:
            color = "Blue"
        elif 190 <= g <= 255:
            color = "Green"
        else:
            color = "Red"
        cv2.putText(img, color+" "+name, (cX, cY), font, 0.5, (255, 255, 255), 1)

    cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)

    cv2.imshow("Shapes and centers", img)

cv2.destroyAllWindows()
