import cv2
import dlib
import imutils
import numpy as np
from imutils import face_utils

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 1)

    for face in rects:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()

        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        mx = int( np.mean(shape[:, 0]) )
        my = int( np.mean(shape[:, 1]) )

        for x, y in shape:
            cv2.circle(img, (x, y), 1, (0, 0, 255), 1)
            cv2.line(img, (x, y), (mx, my), (0, 255, 255))

        cv2.circle(img, (mx, my), 1, (255, 0, 0), 5)

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("win", img)
    if cv2.waitKey(30) == ord('q'):
        break

cv2.destroyAllWindows()
