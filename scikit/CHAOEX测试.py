import base64
import os
import time
from io import BytesIO

import requests
from PIL import Image, ImageDraw
import numpy as np
from sklearn import neighbors, preprocessing
from sklearn.model_selection import train_test_split, cross_val_score

from scikit.图片识别测试 import createData1
from scikit.生成图片 import iamge2imbw
from sklearn import preprocessing


# 获取图片
def getimg(url='http://www.nb.top/12lian/user/getimg'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.post(url, headers=headers)

    return r.json();


def train():
    X, y = createData1()
    scaler = preprocessing.StandardScaler().fit(X)
    scaler.transform(X)
    knn = neighbors.KNeighborsClassifier()

    knn.fit(X, y)
    return knn, scaler


def score():
    X, y = createData1()
    preprocessing.scale(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    knn = neighbors.KNeighborsClassifier()
    knn.fit(X_train, y_train)
    print(knn.score(X_test, y_test))


def login(url, codid, vercode):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    email = '982973525@qq.com'
    pwd = 'aa64c947ce278ddc0b4418bd186fb1a0'
    data = {'email': email,
            'pwd': pwd,
            'codeid': codid,
            'vercode': vercode,
            'source': 1
            }

    r = requests.post(url, data=data, headers=headers)
    return r.json()


# 将图片分成五份
def spitAndSave(knn=None, scaler=None):
    json = getimg()
    IMGCode = json['attachment']['IMGCode']
    codeUUID = json['attachment']['codeUUID']
    imgdata = base64.b64decode(IMGCode)
    image_data = BytesIO(imgdata)
    im = Image.open(image_data)
    # im.save('../data/verify_code/' + codeUUID + ".jpg")

    py = [];
    for j in range(5):
        box = (20 * j, 00, (1 + j) * 20, 30)
        dm = im.crop(box)
        dm = dm.convert("L")
        dm, rate = iamge2imbw(dm)
        dm.save('../data/chaoex/ ' + str(j) + '_' + codeUUID + ".jpg");

        if knn != None:
            data = [dm.getdata()];
            scaler.transform(data)
            p = knn.predict(data);
            print(p[0])
            dm.save('../data/prdict/' + p[0] + '_' + codeUUID + ".jpg");


# 将图片分成五份
def spit2():
    json = getimg()
    IMGCode = json['attachment']['IMGCode']
    codeUUID = json['attachment']['codeUUID']
    imgdata = base64.b64decode(IMGCode)
    image_data = BytesIO(imgdata)
    im = Image.open(image_data)

    dms = [];
    data = []
    for j in range(5):
        box = (20 * j, 00, (1 + j) * 20, 30)
        dm = im.crop(box)
        dm = dm.convert("L")
        dm, rate = iamge2imbw(dm)
        dms.append(dm)
        data.append(dm.getdata())
    return data, dms, codeUUID;


def create():
    for i in range(10):
        r = getimg();
        t = str(int(time.time() * 1000))

        IMGCode = r['attachment']['IMGCode']
        codeUUID = r['attachment']['codeUUID']
        imgdata = base64.b64decode(IMGCode)
        # filename = os.popen('redis-cli -h 192.168.0.138  get  IMG' + codeUUID).read().strip() + '_' + t + '.jpg'
        filename = codeUUID + '.jpg';
        print(filename)
        file = open('../data/verify_code/' + filename, 'wb')
        file.write(imgdata)
        file.close()


def train_real():
    knn, scaler = train();
    test_x, dms, codeUUID = spit2()
    scaler.transform(test_x)
    vercode = ''.join(knn.predict(test_x))
    print(vercode)

    r = login('http://www.nb.top/12lian/user/login', codeUUID, vercode)
    print(r)
    if r['status'] != 200:
        for i in range(5):
            dms[i].save('../data/prdict/' + vercode[i] + '_' + codeUUID + str(i) + ".jpg");
    else:
        for i in range(5):
            dms[i].save('../data/single_code/' + vercode[i] + '_' + codeUUID + str(i) + ".jpg");


if __name__ == '__main__':
    score()

# spit()
