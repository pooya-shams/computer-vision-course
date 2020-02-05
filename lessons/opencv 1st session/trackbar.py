import cv2

font = cv2.FONT_HERSHEY_TRIPLEX

cv2.namedWindow("window")

img = cv2.imread("1.png")

cv2.createTrackbar("name", "window", 50, 156, lambda x:None)

#cap = cv2.VideoCapture(0)

while True:
    img = cv2.imread("1.png") # will over write if you don't retry this every time
    #img = cap.read()
    x = cv2.getTrackbarPos("name", "window")
    cv2.putText(img, str(x), (200, 200), font, 1, (0, 255, 0), 1)
    cv2.imshow("window", img)
    if cv2.waitKey(30) == ord('q'):
        break

cv2.destroyAllWindows()
#cap.release()
