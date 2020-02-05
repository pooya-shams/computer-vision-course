from skimage import feature
import cv2
import imutils

img = cv2.imread("book2.jpg")
img = imutils.resize(img, 400)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

H, hogImage = feature.hog(img, 9, (10, 10), (2, 2), block_norm="L1", transform_sqrt=True, visualize=True)

cv2.imshow("window", hogImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
