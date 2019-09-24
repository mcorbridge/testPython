from testDateTime import TestPythonTime


class TestClassVSstatic:
    foo = 'foo'
    bar = ...
    qwe = NotImplemented
    rty = None

    def __init__(self):
        print("init TestClassVSstatic")

    @classmethod
    def thisClassMethod(cls):
        print(cls.foo + " " + str(type(cls.foo)))
        print(cls.bar)
        print(cls.qwe)
        print(cls.rty)

    def fooMethod(self):
        print("instance method")

    @staticmethod
    def thisStaticMethod(arg):
        amCarbon = 12.011
        amNitrogen = 14.01
        amOxygen = 15.9994
        switcher = {
            'C': amCarbon,
            'N': amNitrogen,
            'O': amOxygen,
        }
        arg = arg.upper()
        print(switcher.get(arg, "Invalid element"))


TestClassVSstatic.thisStaticMethod('C')
TestClassVSstatic.thisStaticMethod('n')
TestClassVSstatic.thisStaticMethod('O')
TestClassVSstatic.thisStaticMethod('0')

TestClassVSstatic.thisClassMethod()
testClassVSstatic = TestClassVSstatic()
testClassVSstatic.fooMethod()
testClassVSstatic.thisClassMethod()

testPythonTime = TestPythonTime()
testPythonTime.printTime()

TestPythonTime.staticPrintTime()