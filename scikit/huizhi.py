import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

"""
绘制一元函数图像y=ax+b

"""


def test():
    plt.figure()  # 实例化作图变量
    plt.title('single variable')  # 图像标题
    plt.xlabel('x')  # x轴文本
    plt.ylabel('y')  # y轴文本
    plt.axis([0, 5, 0, 10])  # x轴范围0-5，y轴范围0-10
    plt.grid(True)  # 是否绘制网格线
    xx = np.linspace(0, 5, 10)  # 在0-5之间生成10个点的向量
    plt.plot(xx, 2 * xx, 'g-')  # 绘制y=2x图像，颜色green，形式为线条
    plt.show()  # 展示图像.


"""
绘制正弦曲线y=sin(x)
"""


def test2():
    plt.figure()  # 实例化作图变量
    plt.title('single variable')  # 图像标题
    plt.xlabel('x')  # x轴文本
    plt.ylabel('y')  # y轴文本
    plt.axis([-12, 12, -1, 1])  # x轴范围-12到12，y轴范围-1到1
    plt.grid(True)  # 是否绘制网格线
    xx = np.linspace(-12, 12, 1000)  # 在-12到12之间生成1000个点的向量
    plt.plot(xx, np.sin(xx), 'g-', label="$sin(x)$")  # 绘制y=sin(x)图像，颜色green，形式为线条
    plt.plot(xx, np.cos(xx), 'r--', label="$cos(x)$")  # 绘制y=cos(x)图像，颜色red，形式为虚线
    plt.legend()  # 绘制图例
    plt.show()  # 展示图像
    plt.show()  # 展示图像


def test3():
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1, projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 500)  # theta旋转角从-4pi到4pi，相当于两圈
    z = np.linspace(0, 2, 500)  # z轴从下到上,从-2到2之间画100个点
    r = z  # 半径设置为z大小
    x = r * np.sin(theta)  # x和y画圆
    y = r * np.cos(theta)  # x和y画圆
    ax.plot(x, y, z, label='curve')
    ax.legend()

    plt.show()


def test4():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    xx = np.linspace(0, 5, 10)
    yy = np.linspace(0, 5, 10)
    zz1 = xx
    zz2 = 2 * xx
    zz3 = 3 * xx
    ax.scatter(xx, yy, zz1, c='red', marker='o')  # o型符号
    ax.scatter(xx, yy, zz2, c='green', marker='^')  # 三角型符号
    ax.scatter(xx, yy, zz3, c='black', marker='*')  # 星型符号
    ax.legend()
    plt.show()


def test5():
    plt.figure()
    plt.title("一元二次方程", fontproperties=getChineseFont())
    plt.xlabel("x轴")
    plt.ylabel("y轴")
    plt.axis([-100, 100, 0, 100])
    plt.grid(True)  # 是否绘制网格线
    xx = np.linspace(-100, 100, 1000)  # 在-12到12之间生成1000个点的向量
    print(xx.shape)
    yy=xx*xx+2*xx+1
    print(yy)

    plt.plot(xx, yy, 'g-', label="$sin(x)$")  # 绘制y=sin(x)图像，颜色green，形式为线条
    plt.show()


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')




