from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()

feature = iris.data
labels = iris.target

xtr, xts, ytr, yts = train_test_split(feature, labels, test_size=.33)

clf = svm.SVC(probability=True, gamma="auto")
# svm.SVC(verbose=True)
clf.fit(xtr, ytr)

sc = clf.score(xts, yts)

print(f"Accuracy is: {sc*100}%")

new = np.array([[2.1, 5.3, 5.5, 5.7]])

print("Probabilities are:", clf.predict_proba(new))
# clf.predict()

predicted_labels = clf.predict(xts)
print(accuracy_score(predicted_labels, yts))
