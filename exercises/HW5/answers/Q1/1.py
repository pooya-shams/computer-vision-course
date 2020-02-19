import cv2
from skimage import feature
import imutils
import numpy as np

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)

#numbers_des = []
#numbers_kp  = []
croppeds = []

font = cv2.FONT_HERSHEY_SIMPLEX

lower = np.array([0, 0, 127])
upper = np.array([255, 255, 255])

joined_train_image = np.zeros([100, 100*10, 3], dtype=np.uint8)

for i in range(10):
    img = cv2.imread(f".\\numbers\\{i}.PNG")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, lower, upper)
    mask = cv2.bitwise_not(mask)
    _, cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(cnts, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(cnt)
    img = img[y:y+h, x:x+w]
    # kp, des = sift.detectAndCompute(img, None)
    # numbers_des.append(des)
    # numbers_kp.append(kp)
    img = cv2.resize(img, (100, 100))
    joined_train_image[ 0:100 , i*100:i*100+100 ] = img

joined_train_image = cv2.GaussianBlur(joined_train_image, (3, 3), 6)

#train_kp, train_des = sift.detectAndCompute(joined_train_image, None)
H, hogImage = feature.hog(joined_train_image, 9, (10, 10), (2, 2), block_norm="L1", transform_sqrt=True, visualize=True)
cv2.imshow("window", hogImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()

pic = cv2.imread("pic.PNG")
#pic = cv2.GaussianBlur(pic, (3, 3), 6)
hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(pic, lower, upper)
mask = cv2.bitwise_not(mask)
_, cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in cnts:
    x, y, w, h = cv2.boundingRect(cnt)
    img = pic[y:y+h, x:x+w]
    croppeds.append(img)

for img in croppeds:
    kp, des = sift.detectAndCompute(img, None)
    match = bf.knnMatch(des, train_des, k=2)

    good_features = []

    for m, n in match:
        if m.distance < .7 * n.distance:
            good_features.append(m)

    print(good_features)
    mathcing_result = cv2.drawMatches(img, kp, joined_train_image, train_kp, good_features, None)
    #mathcing_result = imutils.resize(mathcing_result, 1000)

    cv2.imshow("match", mathcing_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
