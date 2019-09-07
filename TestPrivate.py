from firebase import firebase

class TestPrivate:
    totalObjects = 0

    def __init__(self):
        print("this is an exploration of public private variables: " + str(TestPrivate.totalObjects))
        self.__name = ''
        self.__teams = list()
        TestPrivate.totalObjects = TestPrivate.totalObjects + 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, team):
        self.__teams.append(team)

    @classmethod
    def showcount(cls):
        print("Total objects: ", cls.totalObjects)


testPrivate = TestPrivate()
testPrivate.name = 'Wally'
print(testPrivate.name)

testPrivate.teams = 'Bruins'
testPrivate.teams = 'Leafs'

foo = TestPrivate()
bar = TestPrivate()
qqq = TestPrivate()
www = TestPrivate()

TestPrivate.showcount()

print(testPrivate.teams)

class TestStaticMethods:

    foo = 'foo'
    _foo = '_foo'
    ___goo = '___goo'

    def __init__(self):
        print("this is a test of the python static class")

    @staticmethod
    def greet():
        print("Hello!")

print(TestStaticMethods.foo)
print(TestStaticMethods._foo)
