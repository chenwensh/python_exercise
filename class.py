#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import sys
import os

class Student(object):
	'''The student class'''

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' %(self.name, self.score))

class University_Student(Student):
	'''The University_Student based on the Student class'''
	pass

if __name__ == "__main__":
	'''The bleow segment is example of os.fork.'''
	print('Process %s start' %os.getpid())
	pid = os.fork()
	if pid == 0:
		print('I am the child process (%s) and my parent process is %s' %(os.getpid(), os.getppid()))
	else:
		print('I (%s) just created a child process(%s)' %(os.getpid(), pid))
	theo = Student('Theo', 90)
	theo.print_score()

	emma = Student('Emma', 98)
	emma.print_score()