from Foo import FooBar
from Foo import GropKlop

print("bar")

fb = FooBar()
gk = GropKlop()

fb.printFooBar()
gk.printGropKlop()
gk.dopGing(100)
gk.testMikesDict('a', 'b', 'c')
fibVal = gk.fib(10000)
print(fibVal)

class Goo:
    def __init__(self):
        print('Goo constructor')
        self._qqq = ''

    @property
    def get_qqq(self):
        return self._qqq
    def set_age(self, a):
        self._qqq = a
    def del_qqq(self):
        del self._qqq

goo = Goo()
goo.qqq