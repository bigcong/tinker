import numpy as np
import os

# PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。
from PIL import Image, ImageDraw

from scikit.生成图片 import iamge2imbw, clear_noise


def spilt():
    path = '../data/verify_code/'
    lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
    cout = 0

    for i in lists:
        im = Image.open('../data/verify_code/' + i)

        # im.show()
        for j in range(5):
            box = (20 * j, 00, (1 + j) * 20, 30)
            am = im.crop(box);
            dm = im.crop(box)

            fname = i.split("_")[0][j] + "_" + i.split("_")[1]
            dm = dm.convert("L")
            # dm.show()

            dm, rate = iamge2imbw(dm)
            # clear_noise(dm)

            if rate < 0.05 or rate > 1:
                cout = cout + 1
                am.save('../data/chaoex/' + fname)
            else:
                dm.save('../data/single_code/' + fname)

    print(cout)
    print(len(lists) * 5)

    print(cout / (len(lists) * 5))

