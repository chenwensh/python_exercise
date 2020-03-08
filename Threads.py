#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import threading, time

#The balance variable.
balance = 0
#Add lock for more than one threads to access the global resource.
lock = threading.Lock()

def loop():
	print('thread %s is running...' %threading.current_thread().name)
	n = 0
	while n < 5:
		print('thread %s >>> %s' %(threading.current_thread().name, n))
		time.sleep(1)
		n = n + 1
	print('thread %s end.' %threading.current_thread().name)

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100):
		#Before changing the global resource, we try to get the lock for this resource.
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

if __name__ == '__main__':
	print('thread %s is running...' %threading.current_thread().name)
	'''
	t = threading.Thread(target = loop, name = 'LoopThread')
	t.start()
	t.join()
	print('thread %s end.' %threading.current_thread().name)
	'''
	t1 = threading.Thread(target = run_thread, args = (5,))
	t2 = threading.Thread(target = run_thread, args = (10,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)