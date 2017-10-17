import os

from skimage import io
from sklearn.neighbors import KNeighborsClassifier

# fit a k-nearest neighbor model to the data
model = KNeighborsClassifier()

# model.fit(X, y)
print(model)
# make predictions
# expected = y
# predicted = model.predict(X)
# summarize the fit of the model
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))


dir = '/Users/cong/cc/cc/tinker/data/';
files = os.listdir(dir + '/train')

x = []
y = []

for f in files:
    image = dir + "train/" + f
    if (f.find("yes") > 0):
        y.append(1)
    else:
        y.append(0)

    data = io.imread(image).reshape(205*790*4)


    x.append(data)


model.fit(x, y)

testFiles = os.listdir(dir + '/test')
for f in testFiles:
    image = dir + "test/" + f

    sy = 0
    print(image)
    if (f.find("yes") > 0):
        sy = 1
    else:
        sy = 0

    xdata = io.imread(image).reshape(205*790*4)
    py = model.predict(xdata)
    print(py[0],sy)
