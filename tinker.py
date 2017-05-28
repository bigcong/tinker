import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function: None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))  # 定义权重
    biases = tf.Variable(tf.zeros([1, out_size])) + 0.1  # 定义偏差
    Wx_plus_b = tf.matmul(inputs, Weights) + biases  # 输入数据*权重+偏差
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


x_data = np.linspace(-1, 1, 300)[:, np.newaxis]  # 定一个数组，从-1到1，长度为300的，等差数列# 间隔取数

noise = np.random.normal(0, 0.05, x_data.shape)  # -0.005 到+0.05 到正态分布的拟合

y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1])  # 输入值
ys = tf.placeholder(tf.float32, [None, 1])  # 输出值
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # 隐藏层处理
predition = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition), reduction_indices=[1]))#求和，取平均值
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer();
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.show()
