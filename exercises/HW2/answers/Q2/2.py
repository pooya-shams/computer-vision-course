import cv2
import numpy as np

pause = False

vid = cv2.VideoCapture("back.mp4")
ret, frame = vid.read()
if (not ret) or frame is None:
    exit(1)

lower = np.array([127, 127, 127])
upper = np.array([255, 255, 255])


while True:
    if not pause:
        ret, frame2 = vid.read()
        if (not ret) or frame2 is None:
            vid = cv2.VideoCapture("back.mp4")
            ret, frame2 = vid.read()
        gray_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(gray_1, gray_2)
        diff = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)

        diff = cv2.inRange(diff, lower, upper)

        diff = cv2.erode(diff, None, iterations=4)
        diff = cv2.dilate(diff, None, iterations=8)

        masked = cv2.bitwise_or(frame2, frame2, mask=diff)

        cnts, _ = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(cnts) > 0:
            cnts = np.concatenate(cnts)
            cnts_shape = cnts.shape
            a, b = cnts_shape[:2]
            new_shape = (a*b, 2)
            cnts.reshape(new_shape)

            x, y, w, h =  cv2.boundingRect(cnts)
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("masked", masked)
        cv2.imshow("frame", frame2)

    key = cv2.waitKey(30)

    if key == ord('q'):break
    if key == ord(' '):
        pause = not pause

cv2.destroyAllWindows()
