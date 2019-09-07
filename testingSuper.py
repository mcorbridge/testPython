from singleton import Singleton

class BaseKlass:
    def __init__(self):
        print("I am your base class")
        self.singleton = Singleton.getInstance()
        # self.singleton.foo = "foo"

    def superMethod(self):
        print("I am a method in the base class")

    def getModel(self):
        return self.singleton

    def getFoo(self, a, b):
        c = a + b
        return c

class SubKlass(BaseKlass):
    def __init__(self):
        print("I am the sub class")
        super().__init__()
        super().superMethod()
        singleton = super().getModel()
        singleton.foo = "foop"
        print(singleton.foo)

class SubKlassAgain(BaseKlass):
    def __init__(self):
        print("I am another sub class")
        super().__init__()
        super().superMethod()
        self.singleton = super().getModel()
        print(self.singleton.foo)
        if self.singleton.foo != "foop":
            self.singleton.foo = "bar"
        else:
            self.singleton.foo = "gazoo!"

    def getFoo(self, a, b):
        return a**b

    def doBar(self,a,b=None,c=None):
        if (b is None) and (c is None):
            return a
        elif c is None:
            return a*b
        else:
            return a*b*c

    def doGoo(self, *args):
        print(len(args))
        print(type(args))
        for i in args:
            print(i)

subKlass = SubKlass()
print(subKlass.getFoo(56,90))
subKlassAgain = SubKlassAgain()
print(subKlass.singleton.foo)
print(subKlassAgain.getFoo(100,4))
print(subKlassAgain.doBar(99))
print(subKlassAgain.doBar(3))
print(subKlassAgain.doBar(3,3))
print(subKlassAgain.doBar(3,3,3))
subKlassAgain.doGoo(1,3,8,6,5,9,3)
