import cv2
import numpy as np

pause = False

vid = cv2.VideoCapture("eye.mp4")
font = cv2.FONT_HERSHEY_SIMPLEX

ret, img = vid.read()
if (not ret) or img is None:
    exit(1)

h, w = np.shape(img)[:2]

lower = np.array([20, 0, 0])
upper = np.array([140, 255, 80])


while True:
    key = cv2.waitKey(30)
    if key == ord('q'):break
    elif key == ord(' '):
        pause = not pause

    if pause:continue

    height, width = img.shape[:2]
    w2 = width / 2
    h2 = height / 2
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    bin_img = cv2.inRange(hsv_img, lower, upper)

    bin_img = cv2.erode(bin_img, None, iterations=4)
    bin_img = cv2.dilate(bin_img, None, iterations=16)
    bin_img = cv2.erode(bin_img, None, iterations=2)

    cnts, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(cnts) > 0:
        max_contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        M = cv2.moments(max_contour)
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        cv2.circle(img, (cX, cY), 2, (0, 0, 255), -1)
        cv2.line(img, (cX, 0), (cX, h), (0, 0, 255), 1)
        cv2.line(img, (0, cY), (w, cY), (0, 0, 255), 1)

        direction = "center"
        if cX < w2:
            direction = "left"
        elif cX > w2+30:
            direction = "right"
        elif cY < h2-10:
            direction = "up"
        elif cY > h2+10:
            direction = "down"
        else:
            direction = "not detected"
            
        cv2.putText(img, f"Dir: {direction}", (20, 20), font, 0.5, (0, 0, 255), 2)

        (x, y), r = cv2.minEnclosingCircle(max_contour)
        c = int(x), int(y)
        r = int(r)
        cv2.circle(img, c, r, (0, 255, 0), 2)

        rect = cv2.minAreaRect(max_contour)
        box = cv2.boxPoints(rect)
        box = box.astype(int)
        cv2.drawContours(img, [box], -1, (255, 0, 0), 2)

    cv2.imshow("eye", img)

    ret, img = vid.read()
    if (not ret) or img is None:
        vid = cv2.VideoCapture("eye.mp4")
        ret, img = vid.read()

cv2.destroyAllWindows()
