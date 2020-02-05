import cv2
import numpy as np

vid = cv2.VideoCapture("ball.mp4")

ret, img = vid.read()
if (not ret) or img is None:
    exit(1)

lower = np.array([28, 77, 82])
upper = np.array([154, 255, 255])


while True:
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # converts to hsv (hue saturation value)

    bin_img = cv2.inRange(hsv_img, lower, upper) # converts from hsv to binay range

    bin_img = cv2.dilate(bin_img, None, iterations=4)
    bin_img = cv2.erode(bin_img, None, iterations=2)

    and_img = cv2.bitwise_and(img, img, mask=bin_img) # just returns the important parts

    cnts, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    max_contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    M = cv2.moments(max_contour)
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])

    (x, y), r = cv2.minEnclosingCircle(max_contour)
    c = int(x), int(y)
    r = int(r)
    cv2.circle(img, c, r, (0, 255, 0), 2)

    #cv2.drawContours(img, [max_contour], -1, (0, 0, 255), 2)
    cv2.circle(img, (cX, cY), 2, (0, 0, 255), -1)

    #x, y, w, h =  cv2.boundingRect(max_contour)
    #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    rect = cv2.minAreaRect(max_contour)
    box = cv2.boxPoints(rect)
    box = box.astype(int)
    cv2.drawContours(img, [box], -1, (255, 0, 0), 2)

    cv2.imshow("ball", img)
    if cv2.waitKey(30) == ord('q'):break

    ret, img = vid.read()
    if (not ret) or img is None:
        vid = cv2.VideoCapture("ball.mp4")
        ret, img = vid.read()

cv2.destroyAllWindows()
