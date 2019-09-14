from firebase import firebase
import time


class TestFirebase:
    def __init__(self):
        print("This is an attempt to connect to Firebase")
        try:
            fbTest = firebase.FirebaseApplication('https://wally-97049.firebaseio.com/', None)
            result = fbTest.get('/users', None)
            print(result)
            print(type(result))

            for key in result:
                print(key, '->', result[key]['date_of_birth'])
        except Exception as e:
            print(e.args[0])


testFirebase = TestFirebase()

class WhatAreKwargs:

    def __init__(self):
        print("What the hell are *kwargs?")

    @classmethod
    def testKwargs(self, *kwargs):
        if len(kwargs) == 0:
            print("no args")
        elif (len(kwargs) == 1):
            print("one args")
        elif (len(kwargs) == 2):
            print("two args")
        elif (len(kwargs) == 3):
            print("three args")
        elif (len(kwargs) == 4):
            print("four args")
        else:
            print("more than 4 args")

    @classmethod
    def testDictKwards(self,**kwargs):
        print("\nData type of argument:", type(kwargs))
        for key, value in kwargs.items():
            print("{} is {}".format(key, value))


    @classmethod
    def testTimer(self):
        print("=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8\n")
        for i in reversed(range(1, 11)):
            print(i)
            time.sleep(0.25)



WhatAreKwargs.testKwargs()
WhatAreKwargs.testKwargs(1)
WhatAreKwargs.testKwargs(1,2)
WhatAreKwargs.testKwargs(1,2,3)
WhatAreKwargs.testKwargs(1,2,3,4)

WhatAreKwargs.testDictKwards(Firstname="Moppy", Lastname="Wingawonga", Age=22, Phone=1234567890)
WhatAreKwargs.testDictKwards(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
WhatAreKwargs.testTimer()


class TestSets:
    def __init__(self):
        print("this is a test of the python data type 'sets' ")

    @classmethod
    def makeSet(cls):
        s0 = set()
        s0.add('Herta')
        s0.add('Hinchcliff')
        s0.add('Dixon')
        s0.add('Rossi')
        s0.add('Fanucci')
        s0.add('Herta')
        s0.add('Newgarden')

        s1 = set()
        s1.add('Power')
        s1.add('Kanaan')
        s1.add('Chilton')
        s1.add('Bourdais')
        s1.add('Pagenaud')
        s1.add('Rosenqvist')
        s1.add('Rosenqvist')
        s0.add('Newgarden')

        r = s0.difference(s1)
        print(r)

        r = s0.discard(s1)
        print(r)

        print(s0.intersection(s1))

    @classmethod
    def makeAnotherSet(self):
        s = {'Power','Kanaan','Chilton','Bourdais','Pagenaud','Rosenqvist','Bourdais','Rosenqvist','Chilton','Sato','Andretti','Rahal'}
        print(s)

TestSets.makeSet()
TestSets.makeAnotherSet()

