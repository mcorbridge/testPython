
# testing the concept of python global

import time

i = 0
n = 0

def f():
	global i
	global n
	i += 1
	n += 1
	return "file:" + str(i + n)
	
class Foo:
	i = 0
	n = 0
	
	@classmethod
	def f(self):
		self.i += 1
		self.n += 1
		return "klass:" + str(i + n)
		
	def g(self):
		l = [0,1,2,3,4,5,6,7,8,9]
		print list(enumerate(l))
		for i in l:
			print "----> forLoop:" + str(i)
			time.sleep(0.1)
			
class C(object):
	def __init__(self):
		self._x = None

	@property
	def x(self):
		"""I'm the 'x' property."""
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@x.deleter
	def x(self):
		del self._x
		
class G(object):
	speedOfLight = 299792458
	
	@staticmethod
	def f(arg1, arg2):
		return arg1 + " " + arg2

if __name__ == "__main__":
	print(__name__)
	print "************************"
	while True:
		print str(f())
		foo = Foo()
		print dir(foo)
		print(foo.f())
		foo.g()
		time.sleep(1)
		c = C()
		print str(c.x)
		c.x = 0
		print str(c.x)
		print G.f("the rain in spain"," falls mainly on the plain")
		print str(G.speedOfLight)