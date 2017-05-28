import tensorflow as tf


def add_layer(inputs, in_size, out_size, activation_funciton=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros(1, out_size) + 0.1, )
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_funciton is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_funciton(Wx_plus_b, )
    return outputs
