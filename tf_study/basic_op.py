#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import tensorflow as tf

# Key components in tensorflow: Graph,op,Session,tensor,variable,feed/fetch.
# Graph:the computation task;
# Session: in which context,the Graph will be taken. The session will dispatch the op to GPU/CPU...
# op:the operation entity with some compute function.
# Tensor:the data input to op or output of op;
# Variable: store the staus of the Graph computation.
# Feed: set the tensor data to arbitray operation.
# Fetch: get the tensor data from arbitray operation.

# Define two constant ops as source op.
# Source op don't need the input.
# Usually the constant op will taken as the source op.source.
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

# Define one matmul op.
product = tf.matmul(matrix1, matrix2)

# Start the default graph.
with tf.Session() as sess:
	# Call the run method to run the matmul op.
	result = sess.run(product)
	print(result)
