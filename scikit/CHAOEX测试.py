import base64
import os
import time
from io import BytesIO

import requests
from PIL import Image, ImageDraw
import numpy as np
from sklearn import neighbors

from scikit.图片识别测试 import createData1
from scikit.生成图片 import iamge2imbw

x, y = createData1()
knn = neighbors.KNeighborsClassifier()
knn.fit(x, y);
cout = 0

for i in range(1):
    print("---------------------------")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.post('https://www.chaoex.com/12lian/user/getimg', headers=headers)
    t = str(int(time.time() * 1000))
    print(r.json())

    IMGCode = r.json()['attachment']['IMGCode']
    codeUUID = r.json()['attachment']['codeUUID']
    print('redis-cli   set  codeid ' + codeUUID)

    os.popen('redis-cli   set  codeid ' + codeUUID)
    imgdata = base64.b64decode(IMGCode)


    vercode = os.popen('redis-cli -h 192.168.0.138  get  IMG' + codeUUID).read().strip();
    filename = os.popen('redis-cli -h 192.168.0.138  get  IMG' + codeUUID).read().strip() + '_' + t + '.jpg'
    image_data = BytesIO(imgdata)

    im = Image.open(image_data)
    db=im;

    py = [];
    for j in range(5):
        box = (20 * j, 00, (1 + j) * 20, 30)
        dm = im.crop(box)
        dm = dm.convert("L")

        dm, rate = iamge2imbw(dm)

        data = np.matrix(dm.getdata(), dtype='float') / 225  # 转换成矩阵
        dm.save('../data/chaoex/' + knn.predict(data[0])[0] + ".jpg")

        py.append(np.array(data)[0])
    p = ''.join(knn.predict(py))

    if p == vercode:
        cout = cout + 1

    else:
        print("实际验证码：" + vercode)
        print("预测值：" + p)
    os.popen('redis-cli   set  vercode ' + p)
    im.save('../data/chaoex/' + p+".jpg")



print(cout / 100)
