import cv2
import dlib
import imutils
from imutils import face_utils
from scipy.spatial import distance as dis

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3

COUNTER = 0
TOTAL = 0

def eye_aspect_reatio(eye):
    A = dis.euclidean(eye[1], eye[5])
    B = dis.euclidean(eye[2], eye[4])
    C = dis.euclidean(eye[0], eye[3])
    ear = (A+B)/(2*C)
    return ear


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

video = "eye2.mp4"
vid = cv2.VideoCapture(video)

default_angle = -90
rotation_angle = 0

p = False
width = 800
font = cv2.FONT_HERSHEY_COMPLEX

while True:
    key = cv2.waitKey(3)
    if key == ord('p') or key == ord(' '):
        p = not p
    if key == ord('q'):
        break
    if p:
        continue
    _, img = vid.read()
    if img is None:
        vid = cv2.VideoCapture(video)
        _, img = vid.read()

    img = imutils.resize(img, width)
    img = imutils.rotate(img, default_angle+rotation_angle)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)

    for face in rects:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        lefteye  = shape[36:42]
        righteye = shape[42:48]

        leftEAR = eye_aspect_reatio(lefteye)
        rightEAR = eye_aspect_reatio(righteye)

        ear = (leftEAR + rightEAR) / 2

        leftHull = cv2.convexHull(lefteye)
        rightHull = cv2.convexHull(righteye)

        cv2.drawContours(img, [leftHull], -1, (255, 255, 0))
        cv2.drawContours(img, [rightHull], -1, (255, 255, 0))

        if ear < EYE_AR_THRESH:
            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1
            COUNTER = 0

    cv2.putText(img, f"Blink: {TOTAL}", (20, 20), font, 0.5, (255, 0, 255), 1)
    cv2.imshow("frame", img)

cv2.destroyAllWindows()
