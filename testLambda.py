class TestLambda:
    def __init__(self):
        print("this is a test of python lambda functions")

    def sampleOne(self):
        x = lambda a: a + 10
        print(x(5))

        sum = lambda x, y: x + y

        print(sum(99, 99))

        self.sampleTwo(sum)

    def fahrenheit(T):
        return ((float(9) / 5) * T + 32)

    def celsius(T):
        return (float(5) / 9) * (T - 32)

    temperatures = (36.5, 37, 37.5, 38, 39)

    F = map(fahrenheit, temperatures)
    C = map(celsius, F)

    print(F)
    print(C)

    n = 0
    for t in F:
        print(str(temperatures[n]) + '°C = ' + str(t) + '°F')
        n = n + 1

    for t in C:
        print(t)

    def sampleTwo(self, lbda):
        print(lbda(100, 100))


testLambda = TestLambda()
testLambda.sampleOne()

print("--------------------------------------------------")

foo = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
bar = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
qwe = ('nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'zero')


def doFooBar(a, b, c):
    return str(a) + ":" + str(b) + " " + c


r = (map(doFooBar, foo, bar, qwe))

for t in r:
    print(t)

row1 = ([1, 1, 'o', 0], [1, 2, 'o', 0], [1, 3, 'o', 0], [1, 4, 'o', 0], [1, 5, 'o', 0])
row2 = ([2, 1, 'x', 0], [2, 2, 'x', 0], [2, 3, 'o', 0], [2, 4, 'o', 0], [2, 5, 'o', 0])
row3 = ([3, 1, 'x', 0], [3, 2, 'x', 0], [3, 3, 'o', 0], [3, 4, 'o', 0], [3, 5, 'o', 0])
row4 = ([4, 1, 'o', 0], [4, 2, 'o', 0], [4, 3, 'o', 0], [4, 4, 'o', 0], [4, 5, 'o', 0])
row5 = ([5, 1, 'o', 0], [5, 2, 'o', 0], [5, 3, 'o', 0], [5, 4, 'o', 0], [5, 5, 'o', 0])

#               o o o o o
#               x x o o o
#               x x o o o
#               o o o o o

square = (row1, row2, row3, row4, row5)

print("=========================================================================")

islandNum = 1


def islandFinder(row1, row2, row3, row4, row5):
    global islandNum

    if row1[2] == 'x':
        row1[3] = islandNum
        islandNum += 1

    if row2[2] == 'x':
        row2[3] = islandNum
        islandNum += 1

    if row3[2] == 'x':
        row3[3] = islandNum
        islandNum += 1

    if row4[2] == 'x':
        row4[3] = islandNum
        islandNum += 1

    if row5[2] == 'x':
        row5[3] = islandNum
        islandNum += 1

    return row1, row2, row3, row4, row5


test = map(islandFinder, row1, row2, row3, row4, row5)

for i in test:
    print(i)
