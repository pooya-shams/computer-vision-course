import cv2
import numpy as np

img = np.zeros((200, 300, 3), np.uint8)

cv2.namedWindow("window")
cv2.imshow("window", img)

cv2.createTrackbar("Power", "window", 0, 1, lambda x:None)
cv2.createTrackbar('R', "window", 0, 255, lambda x:None)
cv2.createTrackbar('G', "window", 0, 255, lambda x:None)
cv2.createTrackbar('B', "window", 0, 255, lambda x:None)

while True:
    r = cv2.getTrackbarPos('R', "window")
    g = cv2.getTrackbarPos('G', "window")
    b = cv2.getTrackbarPos('B', "window")
    a = cv2.getTrackbarPos("Power", "window")
    if a:
        img[:,:,:] = b, g, r
    cv2.imshow("window", img)
    if cv2.waitKey(30) == ord('q'):
        break

cv2.destroyAllWindows()
