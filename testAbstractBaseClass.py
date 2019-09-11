from abc import ABC, abstractmethod

# #####################################################
class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def do_anything(self):
        pass

# #####################################################
class Foo(AbstractClassExample):

    def __init__(self):
        print("Foo constructor")

    def do_something(self):
        print("Foo did something")

    def do_anything(self):
        return "anything"

foo = Foo()
foo.do_something()
print("[" + foo.do_anything() + "]")