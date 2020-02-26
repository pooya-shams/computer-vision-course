import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
pause = False

lower = np.array([0, 0, 0])
upper = np.array([255, 255, 100])

while True:
    key = cv2.waitKey(30)
    if key == ord('q'):break
    elif key == ord(' '):
        pause = not pause
    if pause:
        continue

    img = cv2.imread("1.jpg")

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    bin_img = cv2.inRange(hsv_img, lower, upper)

    not_bin_img = cv2.bitwise_not(bin_img)

    cnts, _ = cv2.findContours(not_bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in cnts:
        M = cv2.moments(cnt)
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        cv2.circle(img, (cX, cY), 2, (255, 255, 255), 5)
        cv2.putText(img, "Center", (cX, cY-10), font, .5, (255, 255, 255), 1)

    cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)

    cv2.imshow("Shapes and centers", img)

cv2.destroyAllWindows()
