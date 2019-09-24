import math
import sys
import fibo
import myModule


print(math.pi)
print(math.pi * 2)

print(sys.path)

print("")
print("Arithmetic operators in Python")
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)
# Output: x - y = 11
print('x - y =',x-y)
# Output: x * y = 60
print('x * y =',x*y)
# Output: x / y = 3.75
print('x / y =',x/y)
# Output: x // y = 3
print('x // y =',x//y)
# Output: x ** y = 50625
print('x ** y =',x**y)

print("")
print("Python Namespace and Scope")
a = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

# global namespace
global a
a = "foo is foo"
print(a)

# call function
print("Call an imported function")
fibo.fib(1000)

ob = fibo.MyClass()
ob.func()

foo = fibo.FooClass()
aFoo = foo.fooFunction("Gazooey!")
print(aFoo)

class QQ:
	def doQue(self):
		foo = fibo.FooClass()
		aFoo = foo.fooFunction("Gazooey!")
		print(aFoo)

q = QQ()
q.doQue()

# ############################################################
print("test myModule")

print(myModule.func1())

print(myModule.func2("Hello World!"))

r = myModule.Square(5)
print (r.length)  # automatically calls getter
r.length = 6  # automatically calls setter
print (r.length)  # automatically calls getter

print

starBucksCup = myModule.CoffeeCup()
starBucksCup.color = "white"
print (starBucksCup.color)
starBucksCup.content = "coffee"
print (starBucksCup.content)
starBucksCup.empty()
starBucksCup.fill("coffee")


