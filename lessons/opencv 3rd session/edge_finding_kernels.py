import cv2
import imutils

img = cv2.imread("flowers.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, dx=1, dy=1, ksize=3)
canny = cv2.Canny(gray, 10, 100)
imutils_edge = imutils.auto_canny(img)

cv2.imshow("canny", canny)
cv2.imshow("sobel", sobel)
cv2.imshow("imutils edge", imutils_edge)
cv2.waitKey()
cv2.destroyAllWindows()
