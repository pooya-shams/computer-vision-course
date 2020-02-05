import cv2

# print(cv2.__version__)

"""img = cv2.imread("1.png") # reads image -> (directory)

x = img[10, 20]

print(x)

cv2.imshow("image_window", img) # shows image -> (window name, image matrix)

cv2.waitKey(1000) # will return the pressed key and time.sleep if the argument is not 0, wont work if there is no image, will return the pressed key if argument is 0 -> (miliseconds)

cv2.waitKey(0)

cv2.destroyWindow("image_window") # destroys the window -> (window name)

cv2.destroyAllWindows() # destroys all windows -> ()

cv2.imwrite("2.jpg", img) # will write the image on hard drive, changes the format if the name contains different extension -> (file name, image matrix)
"""

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
