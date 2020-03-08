#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelBinarizer

def add_layer(inputs, in_size, out_size, layer_name, dropout = 1, activiation_function = None):
	Weights = tf.Variable(tf.random_normal([in_size, out_size]))
	biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, )
	Wx_plus_b = tf.matmul(inputs, Weights) + biases

	# Dropout
	Wx_plus_b = tf.nn.dropout(Wx_plus_b, dropout)

	if activiation_function is None:
		outputs = Wx_plus_b
	else:
		outputs = activiation_function(Wx_plus_b)

	tf.summary.histogram(layer_name + '/outputs', outputs)
	return outputs

if __name__ == '__main__':
	# Load data
	digits = load_digits()
	x = digits.data
	y = digits.target
	y = LabelBinarizer().fit_transform(y)
	X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.3)

	# Define the placeholder for inputs to network
	keep_prob = tf.placeholder(tf.float32)
	xs = tf.placeholder(tf.float32, [None, 64]) # 8 * 8
	ys = tf.placeholder(tf.float32, [None, 10])

	# Add output layer
	l1 = add_layer(xs, 64, 50, 'l1', keep_prob, activiation_function = tf.nn.tanh)
	prediction = add_layer(l1, 50, 10, 'l2', keep_prob, activiation_function = tf.nn.softmax)

	# The loss
	cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), 
		reduction_indices = [1]))

	tf.summary.scalar('loss', cross_entropy)

	train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

	sess = tf.Session()
	merged =  tf.summary.merge_all()

	train_writer = tf.summary.FileWriter("logs/train", sess.graph)
	test_writer = tf.summary.FileWriter("logs/test", sess.graph)

	sess.run(tf.global_variables_initializer())

	for i in range(500):
		# Here to determine the keeping probability
		sess.run(train_step, feed_dict = {xs : X_train, ys : y_train, keep_prob : 1})
		if i % 50 == 0:
			# Record the loss
			train_result = sess.run(merged, feed_dict = {xs : X_train, ys : y_train, keep_prob : 1})
			test_result = sess.run(merged, feed_dict = {xs : X_test, ys : y_test, keep_prob : 1})
			train_writer.add_summary(train_result, i)
			test_writer.add_summary(test_result, i)

