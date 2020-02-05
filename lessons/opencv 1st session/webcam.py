import cv2


cap = cv2.VideoCapture(0) # 0 will read webcam, other numbers will read other cameras, IP addres will read ip camera's webcam, video directory will read a video -> (argument)

while True:

    ret, frame = cap.read() # will read the object

    if frame is None:break

    cv2.imshow("image window", frame)

    a = cv2.waitKey(30)

    if a == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
