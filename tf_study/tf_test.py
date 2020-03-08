#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys

FLAGS = None

# Define the add layer function that shows how to transfer the linear to nolinear function.k
def add_layer(input, in_size, out_size, activation_function = None):
	Weights = tf.Variable(tf.random_normal([in_size, out_size]))
	biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
	Wx_plus_b = tf.matmul(input, Weights) + biases
	
	if activation_function is None:
		outputs = Wx_plus_b
	else:
		# Call activation function to transfer the linear to nonlinear.
		outputs = activation_function(Wx_plus_b)
	
	return outputs

def has_layer_model():
	# Define the input and output train data.
	x_train = np.linspace(-1, 1, 300, dtype = np.float32)[:, np.newaxis]
	noise = np.random.normal(0, 0.05, x_train.shape).astype(np.float32)
	y_train = np.square(x_train) - 0.5 + noise
	#print("x_train:", x_train, "y_train:", y_train)

	# Define the x and y placeholder
	x = tf.placeholder(tf.float32, [None, 1])
	y = tf.placeholder(tf.float32, [None, 1])

	# Define the hidden layer and prediction layer
	l1 = add_layer(x, 1, 10, activation_function = tf.nn.tanh)
	prediction = add_layer(l1, 10, 1, activation_function = None)

	# Loss function
	loss = tf.reduce_mean(tf.reduce_sum(tf.square(y - prediction), reduction_indices = [1]))

	# Select the optimizer
	optimizer = tf.train.GradientDescentOptimizer(0.1)
	train_step = optimizer.minimize(loss)

	# Define the session
	init = tf.global_variables_initializer()
	sess = tf.Session()
	sess.run(init)

	# Show the traing status
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.scatter(x_train, y_train)
	plt.ion()
	plt.show()

	# Train the model
	for step in range(5000):
		sess.run(train_step, feed_dict = {x : x_train, y : y_train})
		if step % 100 == 0:
		#	print(sess.run(loss, feed_dict = {x : x_train, y : y_train}))
			try:
				ax.lines.remove(lines[0])
			except Exception:
				pass
			prediction_value = sess.run(prediction, feed_dict = {x : x_train})
			lines = ax.plot(x_train, prediction_value, 'r-', lw = 5)
			plt.pause(0.1)


def linear_regression_model():
	# Model parameters
	W = tf.Variable([.3], tf.float32)
	b = tf.Variable([-.3], tf.float32)

	# Model input and output
	x = tf.placeholder(tf.float32)
	y = tf.placeholder(tf.float32)
	linear_model = x * W + b

	# Loss function
	loss = tf.reduce_sum(tf.square(linear_model - y))

	# Optimizer
	optimizer = tf.train.GradientDescentOptimizer(0.01)
	train = optimizer.minimize(loss)
	
	# Training data
	x_train = [1,2,3,4]
	y_train = [0,1,2,3]

	# Traing loop
	init = tf.global_variables_initializer()
	sess = tf.Session()
	sess.run(init)

	for step in range(1000):
		sess.run(train, {x:x_train, y:y_train})
		if step % 100 == 0:
			curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})
			print("Current W is %s, current b is %s, current loss is %s."%(curr_W, curr_b, curr_loss))
	
def linear_simple_model1():
	# Create the training data
	x_data = np.random.rand(100).astype(np.float32)
	y_data = x_data * 0.1 + 0.3

	# Create the tensorflow structure
	Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
	biases = tf.Variable(tf.zeros([1]))

	y = x_data * Weights + biases
	
	loss = tf.reduce_mean(tf.square(y - y_data))
	optimizer = tf.train.GradientDescentOptimizer(0.5)
	train = optimizer.minimize(loss)

	# init = tf.initialize_all_variables()
	sess = tf.Session()
	
	init = tf.global_variables_initializer()
	sess.run(init)

	for step in range(201):
		sess.run(train)
		if step % 20 == 0:
			print(step, sess.run(Weights), sess.run(biases))

def main(_):
	# Call the function with the function's string name from input parameter
	globals()[FLAGS.model_name]()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--model_name',
		type = str,
		default = 'linear_simple_model1',
		help = 'Model name:linear_simple_model1,linear_regression_model,has_layer_model.More will be added soon.'
	)
	
	FLAGS, unparsed = parser.parse_known_args()
	tf.app.run(main = main, argv = [sys.argv[0]] + unparsed)