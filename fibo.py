

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
	
class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')
		
class FooClass:
	"This is my FooClass"
	def fooFunction(self,a):
		return (a + " is foo!!")
		
if __name__ == "__main__":
	fib(100)
	print str(fib2(100))
	myClass = MyClass()
	myClass.func()
	fooClass = FooClass()
	print fooClass.fooFunction("Wlly")