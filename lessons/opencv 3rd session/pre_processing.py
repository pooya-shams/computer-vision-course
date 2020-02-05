import cv2
import imutils

img = cv2.imread("flowers.png")

translated_img = imutils.translate(img, 100, -70)
rotated_img = imutils.rotate(img, 60)
resized_img = imutils.resize(img, 400)
#google_logo = imutils.url_to_image("url/to/image")


cv2.imshow("translated", translated_img)
cv2.imshow("rotated", rotated_img)
cv2.imshow("resized", resized_img)
cv2.waitKey()
cv2.destroyAllWindows()
