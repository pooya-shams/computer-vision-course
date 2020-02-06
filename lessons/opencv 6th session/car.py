import cv2
from skimage import feature
from sklearn import svm
import glob
import numpy as np
import pickle
import os

pics = []
labels = []
font = cv2.FONT_HERSHEY_SIMPLEX

def pre_proccess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (100, 40))
    hog = feature.hog(img)
    hog = np.array([hog])
    return hog

def extract_features(type_of_image):
    for pic in glob.glob(os.path.join("CarData", "TrainImages", "{}-*.pgm".format(type_of_image))):
        img = cv2.imread(pic)
        vector = feature.hog(img)
        pics.append(vector)
        if type_of_image == "pos": labels.append("Car")
        else: labels.append("nonCar")

extract_features("neg")
extract_features("pos")

#clf = svm.SVC(gamma="auto")

#clf.fit(pics, labels)

#pickle.dump(clf, open("model.pkl", "wb"))

clf = pickle.load(open("model.pkl", "rb"))

print("[INFO : Training was completed!]")

for i in range(1, 19):
    test_img = cv2.imread(os.path.join("Test", "nonCar", "nonCar{}.jpg".format(i)) )
    hog = pre_proccess(test_img)

    out = clf.predict(hog)[0]

    test_img = cv2.resize(test_img, (800, 320))
    cv2.putText(test_img, f"Not Car : {out}", (10, 20), font, .7, (0, 255, 0), 2)
    cv2.imshow("win", test_img)
    cv2.waitKey()

for i in range(1, 14):
    test_img = cv2.imread(os.path.join("Test", "Car", "Car{}.jpg".format(i)))
    hog = pre_proccess(test_img)

    out = clf.predict(hog)[0]

    test_img = cv2.resize(test_img, (800, 320))
    cv2.putText(test_img, f"Car : {out}", (10, 20), font, .7, (0, 255, 0), 2)
    cv2.imshow("win", test_img)
    cv2.waitKey()

cv2.destroyAllWindows()
