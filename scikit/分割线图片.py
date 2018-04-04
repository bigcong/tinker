import numpy as np
import os

# PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。
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

    if near_dots < 2:
        # 确定是噪声,用上面一个点的值代替
        return image.getpixel((x, y - 1))
    else:
        return None


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


def clear_noise(image):
    draw = ImageDraw.Draw(image)
    Width, Height = image.size
    for x in range(Width):
        draw.point((x, 0), 255)
        draw.point((x, Height - 1), 255)
    for y in range(Height):
        draw.point((0, y), 255)
        draw.point((Width - 1, y), 255)

    for x in range(1, Width - 1):
        for y in range(1, Height - 1):
            color = get_near_pixel(image, x, y)
            if color is not None:
                draw.point((x, y), color)


path = '../data/verify_code/'
lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
for i in lists:
    im = Image.open('../data/verify_code/' + i)

    # im.show()
    for j in range(5):
        box = (20 * j, 00, (1 + j) * 20, 30)
        dm = im.crop(box)
        fname = i.split("_")[0][j] + "_" + i.split("_")[1]
        dm = dm.convert("L")

        iamge2imbw(dm, 180)

        clear_noise(dm)

        dm.save('../data/single_code/' + fname)

    # dm.show()
