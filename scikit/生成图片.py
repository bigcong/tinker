import collections

import requests
import base64
import os
import time
from PIL import Image, ImageDraw


def get_near_pixel(image, x, y):
    pix = image.getpixel((x, y))

    near_dots = 0
    if pix == image.getpixel((x - 1, y - 1)):
        near_dots += 1
    if pix == image.getpixel((x - 1, y)):
        near_dots += 1
    if pix == image.getpixel((x - 1, y + 1)):
        near_dots += 1
    if pix == image.getpixel((x, y - 1)):
        near_dots += 1
    if pix == image.getpixel((x, y + 1)):
        near_dots += 1
    if pix == image.getpixel((x + 1, y - 1)):
        near_dots += 1
    if pix == image.getpixel((x + 1, y)):
        near_dots += 1
    if pix == image.getpixel((x + 1, y + 1)):
        near_dots += 1

    if near_dots < 4:
        # 确定是噪声,用上面一个点的值代替
        return image.getpixel((x, y - 1))
    else:
        return None


def clear_noise(image):
    draw = ImageDraw.Draw(image)
    Width, Height = image.size
    for x in range(1, Width - 1):
        for y in range(1, Height - 1):
            color = get_near_pixel(image, x, y)
            if color is not None:
                draw.point((x, y), color)


def iamge2imbw(img, inde=1):
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L")  # 转灰度
    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    total = 0
    a = 0;
    b = 1;

    gg = []
    for y in range(h):
        for x in range(w):
            gg.append(pixdata[x, y])

    g = collections.Counter(gg)

    threshold = list(g.most_common())[inde][0]

    for y in range(h):
        for x in range(w):
            if pixdata[x, y] != threshold:
                pixdata[x, y] = 255
                a = a + 1

            else:
                pixdata[x, y] = 0
                b = b + 1;

    if (b / a) < 0.05:
        print("阀值为：" + str(threshold));
        print(g)

    return img, b / a


def create():
    for i in range(100):
        r = requests.post('http://192.168.0.138:3010/sysUser/getimg')
        t = str(int(time.time() * 1000))

        IMGCode = r.json()['attachment']['IMGCode']
        codeUUID = r.json()['attachment']['codeUUID']
        imgdata = base64.b64decode(IMGCode)
        filename = os.popen('redis-cli -h 192.168.0.138  get  IMG' + codeUUID).read().strip() + '_' + t + '.jpg'
        print(filename)

        file = open('../data/verify_code/' + filename, 'wb')

        file.write(imgdata)
        file.close()
