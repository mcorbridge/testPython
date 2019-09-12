
# © michael d corbridge September 2019
# This is a python algorithm to solve a 'dancing links' recursion simulation encapsulated in a 'find islands' problem.
# The algorithm finds cells that share adjacent sides on the xy axis and groups them as islands.
# One important advantage I can see for Python over Java is that Python lists can take any datatype. This means that I
# do not need to create a bunch of Java objects to store the cell / island information


class TestingRecursion:

    def __init__(self):

        self.row0 = [['o', '', 0, (0, 0)], ['o', '', 0, (0, 1)], ['o', '', 0, (0, 2)], ['o', '', 0, (0, 3)],
                     ['o', '', 0, (0, 4)]]
        self.row1 = [['o', '', 0, (1, 0)], ['x', '', 0, (1, 1)], ['x', '', 0, (1, 2)], ['o', '', 0, (1, 3)],
                     ['o', '', 0, (1, 4)]]
        self.row2 = [['o', '', 0, (2, 0)], ['x', '', 0, (2, 1)], ['x', '', 0, (2, 2)], ['o', '', 0, (2, 3)],
                     ['o', '', 0, (2, 4)]]
        self.row3 = [['o', '', 0, (3, 0)], ['x', '', 0, (3, 1)], ['o', '', 0, (3, 2)], ['o', '', 0, (3, 3)],
                     ['o', '', 0, (3, 4)]]
        self.row4 = [['o', '', 0, (4, 0)], ['o', '', 0, (4, 1)], ['o', '', 0, (4, 2)], ['o', '', 0, (4, 3)],
                     ['o', '', 0, (4, 4)]]

        self.row5 = [['o', '', 0, (0, 0)], ['o', '', 0, (0, 1)], ['o', '', 0, (0, 2)], ['o', '', 0, (0, 3)],
                     ['o', '', 0, (0, 4)]]
        self.row6 = [['o', '', 0, (1, 0)], ['x', '', 0, (1, 1)], ['o', '', 0, (1, 2)], ['x', '', 0, (1, 3)],
                     ['o', '', 0, (1, 4)]]
        self.row7 = [['o', '', 0, (2, 0)], ['x', '', 0, (2, 1)], ['o', '', 0, (2, 2)], ['x', '', 0, (2, 3)],
                     ['o', '', 0, (2, 4)]]
        self.row8 = [['o', '', 0, (3, 0)], ['x', '', 0, (3, 1)], ['x', '', 0, (3, 2)], ['x', '', 0, (3, 3)],
                     ['o', '', 0, (3, 4)]]
        self.row9 = [['o', '', 0, (4, 0)], ['o', '', 0, (4, 1)], ['o', '', 0, (4, 2)], ['o', '', 0, (4, 3)],
                     ['o', '', 0, (4, 4)]]

        self.row10 = [['x', '', 0, (0, 0)], ['o', '', 0, (0, 1)], ['o', '', 0, (0, 2)], ['o', '', 0, (0, 3)],
                     ['o', '', 0, (0, 4)]]
        self.row11 = [['o', '', 0, (1, 0)], ['o', '', 0, (1, 1)], ['o', '', 0, (1, 2)], ['o', '', 0, (1, 3)],
                     ['o', '', 0, (1, 4)]]
        self.row12 = [['o', '', 0, (2, 0)], ['o', '', 0, (2, 1)], ['o', '', 0, (2, 2)], ['o', '', 0, (2, 3)],
                     ['o', '', 0, (2, 4)]]
        self.row13 = [['o', '', 0, (3, 0)], ['o', '', 0, (3, 1)], ['o', '', 0, (3, 2)], ['o', '', 0, (3, 3)],
                     ['o', '', 0, (3, 4)]]
        self.row14 = [['o', '', 0, (4, 0)], ['o', '', 0, (4, 1)], ['o', '', 0, (4, 2)], ['o', '', 0, (4, 3)],
                     ['x', '', 0, (4, 4)]]

        # self.square = [self.row0, self.row1, self.row2, self.row3, self.row4]
        # self.square = [self.row5, self.row6, self.row7, self.row8, self.row9]
        self.square = [self.row10, self.row11, self.row12, self.row13, self.row14]

        self.islandNum = 0

    def printSquare(self):
        for row in self.square:
            print(str(row))

    def iterateSquare(self):
        for row in self.square:
            self.iterateRow(row)

    def iterateRow(self, row):
        for cell in row:
            if cell[0] == 'x':
                self.islandNum = self.islandNum + 1
                cell[2] = self.islandNum
                self.xNeighbor(cell)

    def xNeighbor(self, cell):
        if cell[3][0] != 4 and cell[3][1] != 4:
            numCellRbeside = cell[3][1] + 1
            numRowBeneath = cell[3][0] + 1
            cellRbeside = self.square[cell[3][1]][numCellRbeside]
            cellBelow = self.square[numRowBeneath][cell[3][1]]
            adjacentCells = []

            if cellRbeside[0] == 'x' and cellRbeside[2] == 0:
                cellRbeside[2] = self.islandNum
                adjacentCells.append(cellRbeside)

            if cellBelow[0] == 'x' and cellBelow[2] == 0:
                cellBelow[2] = self.islandNum
                adjacentCells.append(cellBelow)

            if len(adjacentCells) == 0:
                self.islandNum = self.islandNum + 1
            else:
                # do recursion here !
                for aCell in adjacentCells:
                    self.xNeighbor(aCell)

    def getNumIslands(self):
        print("number of islands = " + str(self.islandNum))


testingRecursion = TestingRecursion()

testingRecursion.iterateSquare()

testingRecursion.printSquare()

testingRecursion.getNumIslands()