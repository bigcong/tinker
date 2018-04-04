import numpy as np


def zhuanzhi():  # zhuanzhi
    a = np.mat([[1, 2], [34, 4]]);
    b = np.transpose(a)
    print(a)
    print(b)


def pinfang():  # 平方
    a = np.array([[2, 1], [0, 1]]);
    c = np.power(a, 5)
    d = np.power(a, 2) * np.power(a, 3)
    print(d)
    print(c)


zhuanzhi()
