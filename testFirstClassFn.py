# testing using functions as first class member

class TestFirstClassFn:

    def __init__(self):
        print("init TestFirstClassFn")

    def passThisInto0(self):
        foo = 'foo'
        bar = 'bar'
        return foo + bar

    def passThisInto1(self):
        foo = self.passThisInto0()
        return foo

    def passedInto(self,fn0,fn1):
        f0 = fn0
        f1 = fn1
        print(f0())
        print(f1())

    def passIntoItself(self, fn=None):
        print("Alice in wonderlad")

testFirstClassFn = TestFirstClassFn()

def thisIsFoo():
    return "this is foo"


testFirstClassFn.passedInto(thisIsFoo, testFirstClassFn.passThisInto1)

testFirstClassFn.passIntoItself(testFirstClassFn.passIntoItself(testFirstClassFn.passIntoItself(testFirstClassFn.passIntoItself())))