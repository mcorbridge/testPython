from collections import deque
import collections as c


class TestingCollections:

    def __init__(self):
        print("init testingLinkedList")

    def testDeque(self):
        n0 = TestNode(0)
        n1 = TestNode(1)
        n2 = TestNode(2)

        l = list([n0, n1, n2])
        d = deque(l)

        n3 = TestNode(3)
        d.append(n3)

        for item in d:
            print(item.n)

        n4 = TestNode(4)
        d.insert(3, n4)

        for item in d:
            print(item.n)

        n5 = TestNode(5)

        d.appendleft(n5)

        for item in d:
            print(item.n)

        n6 = TestNode(6)

        d.append(n6)

        print(d.count(n6))
        print(d.count(n3))

        newList = list([TestNode(7), TestNode(8), TestNode(9), TestNode(10), TestNode(11)])

        d.extend(newList)

        for item in d:
            print(item.n)

        d.remove(n5)

        print('-------------------------------')

        for item in d:
            print(item.n)

        print("length of this deque = " + str(len(d)))

        d.rotate(1)

        print('-------------------------------')

        for item in d:
            print(item.n)

        d.rotate(1)

        print('-------------------------------')

        for item in d:
            print(item.n)

        print('-------------------------------')

        print(d.index(n6))
        print(d[d.index(n6)])
        print(d[d.index(n6)].n)

    def testChainMap(self):

        dic1 = {'a': 1, 'b': 2}
        dic2 = {'a':'foo', 'b': 3, 'c': 4}
        chainMap = c.ChainMap(dic1, dic2)
        print(chainMap)
        print(chainMap.get('a'))
        print(chainMap['a'])
        print(chainMap['b'])
        print(chainMap['c'])


class TestNode:
    def __init__(self, n):
        print("init testNode")
        self.foo = "foo"
        self.bar = "bar"
        self.n = n


testingCollections = TestingCollections()



# testingCollections.testDeque()
testingCollections.testChainMap()
