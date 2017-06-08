import numpy as np
from numpy import dot, transpose
from numpy.linalg import inv
from  sklearn.linear_model import LinearRegression

"""

设计二元一次方程：y=1+2x1+3x2

取样本为(1,1,1),(1,1,2),(1,2,1)，计算得y=(6,9,8)

"""


def test1():
    x = [[1, 1, 1], [1, 1, 2], [1, 2, 1]]
    y = [[3], [3], [6]]
    re = dot(inv(dot(transpose(x), x)), dot(transpose(x), y))
    print(re)


"""
也可以用numpy的最小二乘函数直接计算出β
"""


def test2():
    x = [[1, 1, 1], [1, 1, 2], [1, 2, 1]]
    y = [[6], [9], [8]]
    re = np.linalg.lstsq(x, y)[0]
    print(re)


"""
  scikit-learn的线性模型回归吧

"""


def test3():
    x = [[1, 1, 1], [1, 1, 2], [1, 2, 1]]
    y = [[6], [9], [8]]
    model = LinearRegression()

    model.fit(x,y)
    x2 = [[1, 2, 3]]

    y2 = model.predict(x2)
    print(y2)


if __name__ == '__main__':
    test3()
