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


def iamge2imbw(image, threshold):
    # 设置二值化阀值
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 像素值变为0,1
    image = image.point(table, '1')

    # 像素值变为0,255
    image = image.convert('L')
    return image


for i in range(1000):

    r = requests.get('http://192.168.0.138:8888/dfc/user/getimg')
    t = str(int(time.time()*1000))

    IMGCode = r.json()['attachment']['IMGCode']
    codeUUID = r.json()['attachment']['codeUUID']
    imgdata = base64.b64decode(IMGCode)
    filename = os.popen('redis-cli -h 192.168.0.138  get  IMG' + codeUUID).read().strip() + '_' + t + '.jpg'

    file = open('../data/verify_code/' + filename, 'wb')

    file.write(imgdata)
    file.close()
