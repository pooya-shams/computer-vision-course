import cv2
import imutils
import numpy as np

pause = False

img = cv2.imread("ielts.jpg")
img = imutils.resize(img, height=600)

sift = cv2.xfeatures2d.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)

kp_src, des_src = sift.detectAndCompute(img, None)

cap = cv2.VideoCapture("conv.mp4")
ret, frame = cap.read()
if not ret or frame is None:
    exit(1)
h, w, c = frame.shape

font = cv2.FONT_HERSHEY_SIMPLEX

min_len_matches = 80

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        pause = not pause
    if pause:
        continue

    roi = frame[ h // 6 : h // 6 * 5 , w // 6 : w // 6 * 5]

    kp_des, des_des = sift.detectAndCompute(roi, None)

    match = bf.knnMatch(des_src, des_des, k=2)

    good_features = []

    for m, n in match:
        if m.distance < 0.7 * n.distance:
            good_features.append(m)

    l = len(good_features)
    color = (255, 0, 0)
    if l > min_len_matches:
        color = (0, 255, 0)

    cv2.rectangle(frame, (w//6, h//6), (w//6*5, h//6*5), color, 3)

    cv2.putText(frame, f"{l}", (20, 20), font, 0.8, color, 3)

    cv2.imshow("frame", frame)

    _, frame = cap.read()
    if frame is None:
        cap = cv2.VideoCapture("conv.mp4")
        _, frame = cap.read()


