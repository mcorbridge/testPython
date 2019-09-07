print("foo")

import copy
import random

class FooBar:
    def printFooBar(self):
        print("FooBar")

class GropKlop:

    global addNum
    global i
    addNum = 0

    for i in range(0, 101):
        addNum = addNum + i
        print(i)

    def printGropKlop(self):
        print("the sum of " + str(i) + " numbers is: " + str(addNum))

    def dopGing(self,addNum):
        deepcopy = copy.deepcopy(addNum)
        numCopy = deepcopy
        fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'watermelon', 'grape', 'blueberry',
                  'strawberry', 'raspberry', 'peach']

        for i in range(1, numCopy):
            randInt = random.randint(0, len(fruits)-1)
            fruit = fruits[randInt]
            addNum = addNum - 1
            print("[" + str(randInt) + "] " + fruit + "[" + str(addNum) + "]")

    def testMikesDict(self,a,b,c):
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
        print(dict)
        print("dict['Name']: ", dict['Name'])
        print("dict['Age']: ", dict['Age'])

    def fib(self,n):  # return Fibonacci series up to n
        print('----------------------')
        print(self)
        print('----------------------')
        result = []
        a, b = 0, 1
        while b < n:
            result.append(b)
            a, b = b, a + b
        return result
