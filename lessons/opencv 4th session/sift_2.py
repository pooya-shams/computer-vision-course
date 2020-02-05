import cv2
import imutils

img1 = cv2.imread("book1.jpg")
img2 = cv2.imread("book2.jpg")

img1 = imutils.resize(img1, 400)
img2 = imutils.resize(img2, 600)

sift = cv2.xfeatures2d.SIFT_create() # sift object
kp1, des1 = sift.detectAndCompute(img1, None) # (img, mask) -> returns keypoints
kp2, des2 = sift.detectAndCompute(img2, None)

# matching
# first : sorting -> 
"""bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True) # bf matcher object
match = bf.match(des1, des2) # compares des1 and des2 and returns the matching ones
match = sorted(match, key=lambda x:x.distance) # filtering the mathed keypoints sorting by their distance in two images
"""
# second : lowe ratio test
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
match = bf.knnMatch(des1, des2, k=2)

good_features = []

for m, n in match:
    if m.distance < .7 * n.distance:
        good_features.append(m)

mathcing_result = cv2.drawMatches(img1, kp1, img2, kp2, good_features, None)

cv2.imshow("match", mathcing_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
