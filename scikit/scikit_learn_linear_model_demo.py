import matplotlib.pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties
from  sklearn.linear_model import LinearRegression


# 准备数据
def createData():
    x1 = []
    noise = np.random.rand(10, 1)

    for index in range(10):
        x1.append([index])
    y1 = np.array(x1) + noise
    print(y1)
    return x1,y1


def createData1():
    x = [[1], [2], [3], [4], [5], [6]]
    y = [[1], [2.1], [2.9], [4.2], [5.1], [5.8]]
    return x, y


# 打印数据
def plot(x1, y1, x2, y2):
    font = FontProperties()
    plt.figure()
    plt.title('')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.axis([0, 20, 0, 20])
    plt.grid(True)

    plt.plot(x1, y1, 'k.')  # 实际数据
    plt.plot(x2, y2, 'g-')  # 预测数据
    plt.show()


# 数据匹配
def fit(x1, y1):
    mode = LinearRegression()
    mode.fit(x1, y1)
    return mode;


if __name__ == '__main__':

    x1, y1 = createData()
    mode = LinearRegression()
    mode.fit(x1, y1)
    mode = fit(x1, y1)
    x2 = np.random.randint(20,size=(5,1))
    y2 = mode.predict(x2)  # 预测数据y轴
    plot(x1, y1,x2,y2)
