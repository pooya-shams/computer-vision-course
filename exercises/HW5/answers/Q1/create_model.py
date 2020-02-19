import cv2
from skimage import feature
from sklearn import svm
import pickle

pics = []
labels = []

for i in range(10):
    img = cv2.imread(f".\\numbers\\{i}.PNG")
    cv2.imshow(f"{i}", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    v = feature.hog(img)
    pics.append(v)
    labels.append(i)

clf = svm.SVC(gamma="auto")

clf.fit(pics, labels)

pickle.dump(clf, open("numbers.pkl", "wb"))
