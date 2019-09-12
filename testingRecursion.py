
# © michael d corbridge September 2019
# this is a python algorithm to solve a 'dancing links' recursion simulation encapsulated in a 'find islands' problem
# the algorithm finds cells that share adjacent sides on the xy axis and groups them as islands



class TestingRecursion:

    def __init__(self):

        self.tree = [[['<1c.', '<2c.', '<3c.'], '<1b', ['<1c..', '<2c..', '<3c..']], '1a',
                     [['.1c>', '.2c>', '.3c>'], '1b>', ['..1c>', '..2c>', '..3c>']]]
        self.oak = ['1a', ['1b', '2a', ['1c', '2b', '3a', ['1d', '2c', '3b', '4a', ['1e', '2d', '3c', '4b', '5a',
                                                                                    ['1f', '2e', '3d', '4c', '5b',
                                                                                     '6a']]]]]]
        self.rOak = [[[[[['6a', '5b', ['1z', '2z', '3z'], '3d', '2e', '1f'], '1e', '2d', '3c', '4b', '5a'], '1d', '2c',
                        '3b', '4a'], '1c', ['1x', '2x', '3x'], '3a'], '1b', '2a'], '1a']

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

        self.square = [self.row5, self.row6, self.row7, self.row8, self.row9]
        self.rowCounter = 0
        self.cellCounter = 0
        self.islandNum = 0
        self.seed = True
        self.islandSet = set()

    def testTree(self, tree=None):
        if tree == None:
            print(self.tree)
            tree = self.tree
        for branch in tree:
            if isinstance(branch, list):
                self.testTree(branch)
            else:
                print("[" + str(self.counter) + "] " + branch)
                self.counter = self.counter + 1

    def testOak(self, tree=None):
        if tree == None:
            print(self.oak)
            tree = self.oak
        for branch in tree:
            if isinstance(branch, list):
                self.testOak(branch)
            else:
                print("[" + str(self.kounter) + "] " + branch)
                self.kounter = self.kounter + 1

    def reverseTestOak(self, tree=None):
        if tree == None:
            print(self.rOak)
            tree = self.rOak
        for branch in tree:
            if isinstance(branch, list):
                self.reverseTestOak(branch)
            else:
                print("[" + str(self.rKounter) + "] " + branch)
                self.rKounter = self.rKounter + 1

    def printSquare(self):
        for row in self.square:
            print(str(self.rowCounter) + " " + str(row))

    def iterateSquare(self):
        for row in self.square:
            self.iterateRow(row)

    def iterateRow(self, row):
        for cell in row:
            if cell[0] == 'x':
                # print(cell)
                self.islandSet.add(cell[3])
                self.xNeighbor(cell)

    def xNeighbor(self, cell):
        if cell[3][0] != 4 and cell[3][1] != 4:
            print("find cells to the RIGHT and BELOW " + str(cell))
            numCellRbeside = cell[3][1] + 1
            numRowBeneath = cell[3][0] + 1
            # print("cell R beside " + str(self.square[cell[3][1]][numCellRbeside]))
            # print("cell below " + str(self.square[numRowBeneath][cell[3][1]]))
            cellRbeside = self.square[cell[3][1]][numCellRbeside]
            cellBelow = self.square[numRowBeneath][cell[3][1]]
            if cellRbeside[0] == 'x':
                print("add to set " + str(cellRbeside[3]))
                self.islandSet.add(cellRbeside[3])
            if cellBelow[0] == 'x':
                print("add to set " + str(cellBelow[3]))
                self.islandSet.add(cellBelow[3])
            #     do some recursion here !
            print()

    def inspectSet(self):
        print(self.islandSet)


testingRecursion = TestingRecursion()

testingRecursion.iterateSquare()

testingRecursion.inspectSet()
