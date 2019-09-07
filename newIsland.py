

class FindIslands:
    row1 = list()
    row2 = list()
    row3 = list()
    row4 = list()
    row5 = list()

    matrix = list()

    def makeMatrix(self):
        global row1
        row1 = ([1, 1, 'o', 0], [1, 2, 'o', 0], [1, 3, 'o', 0], [1, 4, 'o', 0], [1, 5, 'o', 0])
        global row2
        row2 = ([2, 1, 'x', 0], [2, 2, 'x', 0], [2, 3, 'o', 0], [2, 4, 'o', 0], [2, 5, 'o', 0])
        global row3
        row3 = ([3, 1, 'o', 0], [3, 2, 'x', 0], [3, 3, 'o', 0], [3, 4, 'o', 0], [3, 5, 'o', 0])
        global row4
        row4 = ([4, 1, 'o', 0], [4, 2, 'o', 0], [4, 3, 'o', 0], [4, 4, 'o', 0], [4, 5, 'o', 0])
        global row5
        row5 = ([5, 1, 'o', 0], [5, 2, 'o', 0], [5, 3, 'o', 0], [5, 4, 'o', 0], [5, 5, 'o', 0])

        global matrix
        matrix = (row1, row2, row3, row4, row5)

        #               o o o o o
        #               x x o o o
        #               o o o o o
        #               o o o o o

    def testZip(self):
        zipped0 = zip(row1, row2)
        for item in zipped0:
            print(item)

        print("--------------------------------")
        zipped1 = zip(row2, row3)
        for item in zipped1:
            print(item)

        print("--------------------------------")
        zipped2 = zip(row3, row4)
        for item in zipped2:
            print(item)

        print("--------------------------------")
        zipped3 = zip(row4, row5)
        for item in zipped3:
            print(item)

        print("--------------------------------")
        zipped4 = zip(row1, row2, row3, row4, row5)
        for item in zipped4:
            print(item)

        print("--------------------------------")


findIslands = FindIslands()
findIslands.makeMatrix()
findIslands.testZip()


