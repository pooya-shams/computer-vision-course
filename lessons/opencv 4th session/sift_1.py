import cv2

img = cv2.imread("ielts.jpg")

sift = cv2.xfeatures2d.SIFT_create() # sift object
# kp = sift.detect(img, None) # (img, mask) -> returns keypoints
kp, des = sift.detectAndCompute(img, None) # (img, mask) -> returns keypoints

cv2.drawKeypoints(img, kp, img) # (input image, keypoints, output image, flag)

cv2.imshow("book  1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
