a = 1
b = 2

def func1():
	return a
	
def func2():
	return b
	
def func2(msg):
	return msg
	
# Implementing Java-style getters and setters
class Square:
	def __init__(self, length):
		self._length = length

	@property
	def length(self):
		return self._length

	@length.setter
	def length(self, value):
		self._length = value

	@length.deleter
	def length(self):
		del self._length
		
# testing private vars and methods
class CoffeeCup:
	def __init__(self):
		self.__color = None
		self.__content = None

	def fill(self, beverage):
		self.__content = beverage

	def empty(self):
		self.__content = None
		
	def getColor(self):
		return self.__color
    