import functools


class TestLambdaMap:

    def __init__(self):
        print("init TestLambdaMap")
        self.sqrTup = NotImplemented
        self.fooLambda = lambda x, y: (x ** 3) * (y ** 4)

    def testOne(self):
        tup = (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
        newtuple = tuple(map(lambda x: x + 3, tup))
        print(newtuple)

        cubeTup = tuple(map(lambda x: x ** 3, newtuple))
        print(cubeTup)

        self.sqrTup = tuple(map(lambda y: y ** 2, cubeTup))
        print(self.sqrTup)

    def testFilter(self):
        tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        def func(x):
            return x >= 2 and x <= 8

        filteredTup = filter(func, tup)
        print(list(filteredTup))

    def testReduce(self):
        r = functools.reduce(lambda a, b: a * b / a + b, self.sqrTup)
        print(r)

    def testingLambda(self):
        print("---------------- testing lambda -----------------")
        sqr = lambda x: x ** 2
        print(sqr(4))
        adder = lambda x, y: x + y
        print(adder(5, 6))
        triadder = lambda x, y, z: x + y + z
        print(triadder(5, 6, 7))

        print(adder(100, 200) + triadder(12, 23, 34))

        print(self.fooLambda(7, 8))

        numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

        filtered_list = list(filter(lambda num: (num > 7), numbers_list))
        print(filtered_list)

        numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

        mapped_list = list(map(lambda num: num % 2, numbers_list))

        print(mapped_list)

        numbers_list0 = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
        numbers_list1 = [4, 6, 64, 10, 11, 16, 12, 49, 13, 17, 0, 9, 21]

        def func(val0, val1):
            if val0 ** 2 == val1:
                return val0

        # using a lambda instead of a func in a map operation AND removing the 'None' values in the list
        mapped_list = list(filter(None, map(lambda x,y: x if x ** 2 == y else None, numbers_list0, numbers_list1)))
        print(mapped_list)


testLambdaMap = TestLambdaMap()
testLambdaMap.testOne()
testLambdaMap.testFilter()
testLambdaMap.testReduce()
testLambdaMap.testingLambda()
