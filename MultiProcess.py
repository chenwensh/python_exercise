#!/usr/bin/env python
# -*- coding:utf-8 -*- 

#mulitprocessing is the module for IPC communication.
import multiprocessing
from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print('Process to write:%s' %os.getpid())
	for value in ['a', 'b', 'c']:
		print('Put %s in queue' %value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read:%s' %os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' %value)

if __name__ == '__main__':
	#Print how may cores we have in this computer.
	print('This computer has %s cores' %multiprocessing.cpu_count())
	q = Queue()
	pw = Process(target = write, args = (q,))
	pr = Process(target = read, args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()