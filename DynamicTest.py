print("this is a test of how python classes are dynamic")

class Foo:

    def __init__(self):
        print("this is the default constructor")
        pass

    littleFoo = 1
    bigFoo = 2
    littleBar = 3


foo = Foo()

print(foo.bigFoo)
print(foo.littleBar)
print(foo.littleFoo)

foo.bigBar = 4

print(foo.bigBar)