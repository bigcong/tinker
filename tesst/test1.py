import tensorflow as tf
import numpy as np


def createData():

    x_data = np.random.rand(100).astype(np.float32)
    y_data = x_data * 0.1 + 0.3
    Weights = tf.Variable(tf.random_uniform([1], -2.0, 3.0))
    biases = tf.Variable(tf.zeros([1]))

    y = Weights * x_data + biases
    loss = tf.reduce_mean(tf.square(y - y_data))
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
    sess = tf.Session()

    init = tf.global_variables_initializer()
    sess.run(init)
    for step in range(10000):
        sess.run(train)
        print(step, sess.run(Weights), sess.run(biases))


if __name__ == '__main__':
    createData()
