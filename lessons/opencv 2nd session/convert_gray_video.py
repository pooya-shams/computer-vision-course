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

    out_img = cv2.bitwise_and(img, img, mask=bin_img) # just returns the important parts

    cv2.imshow("window", out_img)
    if cv2.waitKey(30) == ord('q'):break

    ret, img = vid.read()
    if (not ret) or img is None:
        vid = cv2.VideoCapture("ball.mp4")
        ret, img = vid.read()

cv2.destroyAllWindows()
