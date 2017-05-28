import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def add_layer(inputs, in_size, out_size, activation_funciton=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, )
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_funciton is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_funciton(Wx_plus_b, )
    return outputs


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
xs = tf.placeholder(tf.float32, [None, 784])
ys = tf.placeholder(tf.float32, [None, 10])
prediction = add_layer(xs, 784, 10, activation_funciton=tf.nn.softmax)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
tran = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})  # 预测y值
    print(tf.arg_max(y_pre, 1))
    correct_prediction = tf.equal(tf.arg_max(y_pre, 1), tf.arg_max(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


for i in range(10):
    batch_xs, batch_ys = mnist.train.next_batch(1)
    sess.run(tran, feed_dict={xs: batch_xs, ys: batch_ys})

    print(compute_accuracy(mnist.test.images, mnist.test.labels))
