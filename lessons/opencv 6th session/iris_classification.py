from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris = load_iris()

feature = iris.data
labels = iris.target

xtr, xts, ytr, yts = train_test_split(feature, labels, test_size=.33)

clf = KNeighborsClassifier(n_neighbors=5)

clf.fit(xtr, ytr)

sc = clf.score(xts, yts)

print(f"Accuracy is: {sc*100}%")

new = np.array([[2.1, 5.3, 5.5, 5.7]])

ind = clf.predict(new)[0]

print(ind, iris.target_names[ind])
