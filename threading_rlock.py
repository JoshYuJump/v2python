import threading
import time

class thread_a(threading.Thread):
	def __init__(self):
		super(thread_a, self).__init__()
	
	def run(self):
		print 'thread a begin'
		global x
		rlock.acquire()
		while x < 5:
			x += 1
			print 'a:', x
			time.sleep(1)
		rlock.release()	


class thread_b(threading.Thread):
	def __init__(self):
		super(thread_b, self).__init__()
	
	def run(self):
		print 'thread b begin'
		global x
		# rlock.acquire()
		while x < 10:
			x += 1
			print 'b:', x
			time.sleep(2)
		# rlock.release()			





x = 0
rlock = threading.RLock()	

if __name__ == '__main__':
	thread1 = thread_a()
	thread2 = thread_b()
	thread1.start()
	thread2.start()
		
