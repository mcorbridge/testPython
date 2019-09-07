from singleton import Singleton


class Coffee:


    def __init__(self):
        print(__name__)
        print(self)
        self.singleton = Singleton.getInstance()
        self.foo = 'foo'

    @classmethod
    def coffeeType(cls):
        print(cls)
        print('-------------------------')

    def testSingleton(self):
        print(type(self.singleton))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>> " + self.foo + " <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        self.singleton.bar = 'We do not know.'

coffee = Coffee()

Coffee.coffeeType()

coffee.testSingleton()

class Tea:
    def __init__(self):
        self.singleton = Singleton.getInstance()

    def whoIsBar(self):
        print("Where did Barr go? " + self.singleton.bar)

tea = Tea()
tea.whoIsBar()