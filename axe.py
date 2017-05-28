# -*- coding:utf-8 -*-

from PIL import Image
from pylab import *
import numpy as np
import pytesseract
import os.path
import os


def imgToArry():
    im = Image.open('/Users/bigcong/1.png')
    im = im.crop((80, 200, 980, 600))
    a = array(im.crop((80, 200, 980, 600)))
    print(a)
    imshow(im)
    show()
    print(im.size)


def label():
    im1 = Image.open('/Users/bigcong/1.png')
    im2 = Image.open('/Users/bigcong/2.png')

    im1 = im1.crop((320, 350, 770, 380))
    im2 = im2.crop((320, 350, 770, 380))
    vcode = pytesseract.image_to_string(im1)
    print(vcode)

    a1 = np.array(array(im1))
    a2 = np.array(array(im2))
    print(a1)
    print(a1.var(a1, dtype=np.float64))
    print(a1.var(a2, dtype=np.float64))

    print(np.array_equiv(a1, a2))

    imshow(im1)


def isFail(fileUrl):
    print(fileUrl)
    im1 = Image.open(fileUrl)
    im2 = im1.crop((320, 350, 770, 380))

    try:
        v1 = pytesseract.image_to_string(im2)
        if len(v1) < 5:
            return True;
        else:
            return False
    except:

        return True


def saveSmall(url, newurl=33):
    im1 = Image.open(url)
    im2 = im1.crop((110, 375, 900, 580))
    im2.save(newurl)
    os.system('rm -rf ' + url.replace('x.png','*'))


def go():
    for root, dirs, files in os.walk('img'):
        for f in files:
            if 'x' in f:
                url = 'img/' + f
                x = f
                if isFail(url):
                    y_url = 'img/' + f.replace('x.png', 'y.png')
                    ll = '_no'
                    if isFail(y_url):
                        ll = '_yes'
                    smalUrl = 'data/' + x.replace('.png', '') + ll + '.png'
                    saveSmall(url, smalUrl)


if __name__ == '__main__':
    go()
