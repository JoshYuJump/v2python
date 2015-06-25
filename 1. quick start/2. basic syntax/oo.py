
class  hello(object):

	def __init__(self, name):
		self._name = name
	
	def say_hello(self):
		print 'hello, {}.'.format(self._name)


h = hello("Lucy")

h.say_hello()		
		