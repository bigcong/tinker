from PIL import Image, ImageDraw
import os
import numpy as np

from sklearn import neighbors
import sklearn
from sklearn.datasets import load_iris


def createData1():
    xx = []
    yy = []
    path = '../data/single_code/'
    lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
    for i in lists:
        im = Image.open(path + i)
        data = im.getdata()
        data = np.matrix(data, dtype='float') / 225  # 转换成矩阵
        yy.append(i.split("_")[0])
        xx.append(np.array(data)[0])
    return xx, yy


def testData():
    xx = []
    yy = []
    path = '../data/t/'
    lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
    for i in lists:
        im = Image.open(path + i)
        im = im.convert("L")  # 转成灰色模式
        data = im.getdata()
        data = np.matrix(data, dtype='float') / 225  # 转换成矩阵
        yy.append(i.split("_")[0])
        xx.append(np.array(data)[0])
    return xx, yy


def distance(train, v1):
    d = []
    for v2 in train:
        d.append(np.sqrt(np.sum((v2 - v1) ** 2)))

    return d


def test2():
    xx = []
    yy = []
    path = '../data/verify_code/'
    lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
    for i in lists:
        im = Image.open(path + i)
        xxx = []
        for j in range(5):
            box = (20 * j, 00, (1 + j) * 20, 30)
            dm = im.crop(box)
            dm = dm.convert("L")

            iamge2imbw(dm, 180)
            clear_noise(dm)
            data = dm.getdata()
            data = np.matrix(data, dtype='float') / 225  # 转换成矩阵

            xxx.append(np.array(data)[0])

        xx.append(xxx)
        yy.append(i.split("_")[0])

    return xx, yy


def test():
    x, y = createData1()

    tx1, ty2 = test2()
    count = 0
    err = []
    for index, t in enumerate(tx1):
        p = ''
        for jindex, j in enumerate(t):
            sortd = np.argsort(distance(x, j))

            p = p + y[sortd[0]]

        if p == ty2[index]:
            count = count + 1

        print("预测值:" + p)
        print("实际值:" + ty2[index])
        print("-------------------")
    print(len(tx1))
    print("正确率" + str(count / len(tx1)))


# knn
def testt3():
    x, y = createData1()
    tx1, ty2 = test2()
    knn = neighbors.KNeighborsClassifier()
    knn.fit(x, y);

    count = 0

    for index, t in enumerate(tx1):
        p = ''.join(knn.predict(np.array(t)))
        if p == ty2[index]:
            count = count + 1

        print("预测值:" + p)
        print("实际值:" + ty2[index])
        print("-------------------")
    print(len(tx1))
    print("正确率" + str(count / len(tx1)))
