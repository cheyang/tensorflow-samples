import tensorflow as tf
import numpy as np

train_X = np.linspace(-1, 1, 101)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.33 + 10

X = tf.placeholder("float")
Y = tf.placeholder("float")

with tf.device("/job:ps/task:0/cpu:0"):
    w = tf.Variable(0.0, name="weight")
    b = tf.Variable(0.0, name="reminder")

# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
with tf.device("/job:worker/task:0/gpu:0"):
    init_op = tf.global_variables_initializer()
    cost_op = tf.square(Y - tf.mul(X, w) - b)
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost_op)

with tf.Session("grpc://tf-worker0:2222") as sess:
        sess.run(init_op)
        epoch = 1
        for i in range(10):
            for (x, y) in zip(train_X, train_Y):
                sess.run(train_op, feed_dict={X: x, Y: y})
                print ("Epoch: {}, w: {}, b: {}").format(epoch, sess.run(w), sess.run(b))
                epoch += 1

        print ("Result is w: {}, b: {}").format(sess.run(w), sess.run(b))
