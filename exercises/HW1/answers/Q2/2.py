import cv2
import numpy as np

window_name = "Trackbar Face"
trackbar_name = "type"

cv2.namedWindow(window_name)
cv2.createTrackbar(trackbar_name, window_name, 0, 2, lambda x:None)

img = np.zeros((500, 500, 3), dtype=np.uint8)

img0 = np.full((500, 500, 3), 255, dtype=np.uint8)
img1 = np.full((500, 500, 3), 255, dtype=np.uint8)
img2 = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.circle(img0, (250, 250), 250, (200, 50, 50), 3)
cv2.circle(img1, (250, 250), 250, (200, 50, 50), 3)
cv2.circle(img2, (250, 250), 250, (200, 50, 50), 3)

cv2.circle(img0, (500//3, 500//3), 10, (0, 0, 255), 5)
cv2.circle(img1, (500//3, 500//3), 10, (0, 0, 255), 5)
cv2.circle(img2, (500//3, 500//3), 10, (0, 0, 255), 5)

cv2.circle(img0, (500//3*2, 500//3), 10, (0, 0, 255), 5)
cv2.circle(img1, (500//3*2, 500//3), 10, (0, 0, 255), 5)
cv2.circle(img2, (500//3*2, 500//3), 10, (0, 0, 255), 5)
#
cv2.circle(img0, (500//3, 500//3), 1, (255, 0, 0), 5)
cv2.circle(img1, (500//3, 500//3), 1, (255, 0, 0), 5)
cv2.circle(img2, (500//3, 500//3), 1, (255, 0, 0), 5)

cv2.circle(img0, (500//3*2, 500//3), 1, (255, 0, 0), 5)
cv2.circle(img1, (500//3*2, 500//3), 1, (255, 0, 0), 5)
cv2.circle(img2, (500//3*2, 500//3), 1, (255, 0, 0), 5)
#
cv2.rectangle(img0, (500//2-10, 500//2-50), (500//2+10, 500//2+50), (0, 0, 255), 10)
cv2.rectangle(img1, (500//2-10, 500//2-50), (500//2+10, 500//2+50), (0, 0, 255), 10)
cv2.rectangle(img2, (500//2-10, 500//2-50), (500//2+10, 500//2+50), (0, 0, 255), 10)
#
cv2.rectangle(img0, (500//2-10, 500//2-50), (500//2+10, 500//2+50), (255, 0, 0), 1)
cv2.rectangle(img1, (500//2-10, 500//2-50), (500//2+10, 500//2+50), (255, 0, 0), 1)
cv2.rectangle(img2, (500//2-10, 500//2-50), (500//2+10, 500//2+50), (255, 0, 0), 1)
#
cv2.ellipse(img0, (500//2, 500//3*2), (100, 50), 0, 45, 135, (0, 0, 255), 10)
cv2.ellipse(img1, (500//2, 500//3*2+100), (100, 50), 0, 225, 315, (0, 0, 255), 10)
cv2.rectangle(img2, (500//2-50, 500//2+100), (500//2+50, 500//2+110), (0, 0, 255), 10)

while True:
    x = cv2.getTrackbarPos(trackbar_name, window_name)
    if x == 0:
        cv2.imshow(window_name, img0)
    elif x == 1:
        cv2.imshow(window_name, img1)
    elif x == 2:
        cv2.imshow(window_name, img2)
    else: # this won't never be displayed
        cv2.imshow(window_name, img)
    
    if cv2.waitKey(30) == ord('q'):
        break
