# !/usr/bin/env python
#
# Copyright 2019 Michael D Corbridge.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This is a python algorithm using recursion in a 'find islands' problem in a SQUARE (only!) grid.
# The algorithm finds cells that share adjacent sides on the xy axis and groups them as islands.
# Tree traversal (also known as tree search) is a form of graph traversal and refers to the process of visiting
# (checking and/or updating) each node in a tree data structure, exactly once. Such traversals are classified by the
# order in which the nodes are visited.
# One important advantage I can see for Python over Java is that Python lists can take any datatype. This means that I
# do not need to create a bunch of Java objects to store the cell / island information.


class TestingRecursion:

    # set up the sample grid (square)
    def __init__(self):

        self.row0 = [['x', 0, (0, 0)], ['x', 0, (0, 1)], ['x', 0, (0, 2)], ['x', 0, (0, 3)],['x', 0, (0, 4)]]
        self.row1 = [['x', 0, (1, 0)], ['o', 0, (1, 1)], ['x', 0, (1, 2)], ['o', 0, (1, 3)],['o', 0, (1, 4)]]
        self.row2 = [['x', 0, (2, 0)], ['x', 0, (2, 1)], ['x', 0, (2, 2)], ['x', 0, (2, 3)],['x', 0, (2, 4)]]
        self.row3 = [['o', 0, (3, 0)], ['o', 0, (3, 1)], ['x', 0, (3, 2)], ['o', 0, (3, 3)],['x', 0, (3, 4)]]
        self.row4 = [['x', 0, (4, 0)], ['x', 0, (4, 1)], ['x', 0, (4, 2)], ['x', 0, (4, 3)],['x', 0, (4, 4)]]

        self.row5 = [['o', 0, (0, 0)], ['o', 0, (0, 1)], ['o', 0, (0, 2)], ['o', 0, (0, 3)],['o', 0, (0, 4)]]
        self.row6 = [['o', 0, (1, 0)], ['x', 0, (1, 1)], ['o', 0, (1, 2)], ['x', 0, (1, 3)],['o', 0, (1, 4)]]
        self.row7 = [['o', 0, (2, 0)], ['x', 0, (2, 1)], ['o', 0, (2, 2)], ['x', 0, (2, 3)],['o', 0, (2, 4)]]
        self.row8 = [['o', 0, (3, 0)], ['x', 0, (3, 1)], ['x', 0, (3, 2)], ['x', 0, (3, 3)],['o', 0, (3, 4)]]
        self.row9 = [['o', 0, (4, 0)], ['o', 0, (4, 1)], ['o', 0, (4, 2)], ['o', 0, (4, 3)],['o', 0, (4, 4)]]

        self.row10 = [['o', 0, (0, 0)], ['o', 0, (0, 1)], ['x', 0, (0, 2)], ['o', 0, (0, 3)], ['o', 0, (0, 4)]]
        self.row11 = [['o', 0, (1, 0)], ['o', 0, (1, 1)], ['x', 0, (1, 2)], ['o', 0, (1, 3)], ['o', 0, (1, 4)]]
        self.row12 = [['x', 0, (2, 0)], ['x', 0, (2, 1)], ['x', 0, (2, 2)], ['x', 0, (2, 3)], ['x', 0, (2, 4)]]
        self.row13 = [['o', 0, (3, 0)], ['o', 0, (3, 1)], ['x', 0, (3, 2)], ['o', 0, (3, 3)], ['o', 0, (3, 4)]]
        self.row14 = [['o', 0, (4, 0)], ['o', 0, (4, 1)], ['x', 0, (4, 2)], ['o', 0, (4, 3)], ['o', 0, (4, 4)]]

        self.row15 = [['o', 0, (0, 0)], ['o', 0, (0, 1)], ['o', 0, (0, 2)], ['o', 0, (0, 3)], ['o', 0, (0, 4)]]
        self.row16 = [['o', 0, (1, 0)], ['o', 0, (1, 1)], ['o', 0, (1, 2)], ['o', 0, (1, 3)], ['o', 0, (1, 4)]]
        self.row17 = [['o', 0, (2, 0)], ['x', 0, (2, 1)], ['x', 0, (2, 2)], ['o', 0, (2, 3)], ['o', 0, (2, 4)]]
        self.row18 = [['o', 0, (3, 0)], ['x', 0, (3, 1)], ['x', 0, (3, 2)], ['o', 0, (3, 3)], ['o', 0, (3, 4)]]
        self.row19 = [['o', 0, (4, 0)], ['o', 0, (4, 1)], ['o', 0, (4, 2)], ['o', 0, (4, 3)], ['o', 0, (4, 4)]]

        self.row15 = [['o', 0, (0, 0)], ['o', 0, (0, 1)], ['o', 0, (0, 2)], ['o', 0, (0, 3)], ['o', 0, (0, 4)],['o', 0, (0, 5)], ['o', 0, (0, 6)], ['o', 0, (0, 7)], ['x', 0, (0, 8)], ['x', 0, (0, 9)]]
        self.row16 = [['o', 0, (1, 0)], ['o', 0, (1, 1)], ['o', 0, (1, 2)], ['o', 0, (1, 3)], ['o', 0, (1, 4)],['o', 0, (1, 5)], ['o', 0, (1, 6)], ['o', 0, (1, 7)], ['x', 0, (1, 8)], ['x', 0, (1, 9)]]
        self.row17 = [['x', 0, (2, 0)], ['o', 0, (2, 1)], ['o', 0, (2, 2)], ['o', 0, (2, 3)], ['o', 0, (2, 4)],['o', 0, (2, 5)], ['o', 0, (2, 6)], ['o', 0, (2, 7)], ['o', 0, (2, 8)], ['o', 0, (2, 9)]]
        self.row18 = [['x', 0, (3, 0)], ['o', 0, (3, 1)], ['o', 0, (3, 2)], ['x', 0, (3, 3)], ['o', 0, (3, 4)],['o', 0, (3, 5)], ['o', 0, (3, 6)], ['o', 0, (3, 7)], ['o', 0, (3, 8)], ['o', 0, (3, 9)]]
        self.row19 = [['x', 0, (4, 0)], ['o', 0, (4, 1)], ['o', 0, (4, 2)], ['x', 0, (4, 3)], ['o', 0, (4, 4)],['o', 0, (4, 5)], ['o', 0, (4, 6)], ['o', 0, (4, 7)], ['o', 0, (4, 8)], ['o', 0, (4, 9)]]
        self.row20 = [['x', 0, (5, 0)], ['x', 0, (5, 1)], ['x', 0, (5, 2)], ['x', 0, (5, 3)], ['x', 0, (5, 4)],['x', 0, (5, 5)], ['x', 0, (5, 6)], ['x', 0, (5, 7)], ['x', 0, (5, 8)], ['o', 0, (5, 9)]]
        self.row21 = [['x', 0, (6, 0)], ['o', 0, (6, 1)], ['o', 0, (6, 2)], ['o', 0, (6, 3)], ['o', 0, (6, 4)],['o', 0, (6, 5)], ['o', 0, (6, 6)], ['o', 0, (6, 7)], ['x', 0, (6, 8)], ['o', 0, (6, 9)]]
        self.row22 = [['x', 0, (7, 0)], ['o', 0, (7, 1)], ['o', 0, (7, 2)], ['o', 0, (7, 3)], ['o', 0, (7, 4)],['o', 0, (7, 5)], ['o', 0, (7, 6)], ['o', 0, (7, 7)], ['x', 0, (7, 8)], ['o', 0, (7, 9)]]
        self.row23 = [['o', 0, (8, 0)], ['o', 0, (8, 1)], ['o', 0, (8, 2)], ['o', 0, (8, 3)], ['o', 0, (8, 4)],['o', 0, (8, 5)], ['o', 0, (8, 6)], ['o', 0, (8, 7)], ['o', 0, (8, 8)], ['o', 0, (8, 9)]]
        self.row24 = [['o', 0, (9, 0)], ['o', 0, (9, 1)], ['o', 0, (9, 2)], ['o', 0, (9, 3)], ['o', 0, (9, 4)],['o', 0, (9, 5)], ['o', 0, (9, 6)], ['o', 0, (9, 7)], ['o', 0, (9, 8)], ['o', 0, (9, 9)]]

        self.row25 = [['x', 0, (0, 0)], ['o', 0, (0, 1)], ['o', 0, (0, 2)], ['o', 0, (0, 3)]]
        self.row26 = [['o', 0, (1, 0)], ['x', 0, (1, 1)], ['o', 0, (1, 2)], ['o', 0, (1, 3)]]
        self.row27 = [['o', 0, (2, 0)], ['o', 0, (2, 1)], ['x', 0, (2, 2)], ['o', 0, (2, 3)]]
        self.row28 = [['o', 0, (3, 0)], ['o', 0, (3, 1)], ['o', 0, (3, 2)], ['x', 0, (3, 3)]]

        # self.square = [self.row0, self.row1, self.row2, self.row3, self.row4]
        # self.square = [self.row5, self.row6, self.row7, self.row8, self.row9]
        # self.square = [self.row10, self.row11, self.row12, self.row13, self.row14]
        # self.square = [self.row15, self.row16, self.row17, self.row18, self.row19, self.row20, self.row21, self.row22, self.row23, self.row24]
        self.square = [self.row25, self.row26, self.row27, self.row28]
        self.islandNum = 0
        self.boundary = {"lower":0, "upper":len(self.square) - 1}
        self.recursionLoops = 0

    # print out the square with annotations showing island associations and all cell info
    def printSquare(self):
        for row in self.square:
            print(str(row))

    # print out the square with annotations showing island associations showing only 'x' or 'o'
    def prettyPrintSquare(self):
        for row in self.square:
            xRow = []
            for cell in row:
                xRow.append(cell[0])
            print(xRow)

    # this starts the process to find the islands by viewing each row in the square
    def iterateSquare(self):
        for row in self.square:
            self.iterateRow(row)

    # inspect each cell in the row to determine if it is part of an island ('x')
    def iterateRow(self, row):
        for cell in row:
            if cell[0] == 'x' and cell[1] == 0:
                self.islandNum += 1  # <---- here (only HERE) is where the island number is incremented
                cell[1] = self.islandNum
                self.xNeighbor(cell)

    # inspect the neighbour cells, recursively, directly to the left, right (x-axis) & above, below (y-axis) to determine if
    # those cells have an 'x' property that indicates they should be grouped together as an island
    # This function will be called recursively
    def xNeighbor(self, cell):

        adjacentCells = []  # list to hold the neighbouring cells for the recursion
        cellLeft = [0, 0]  # initialize the cell neighbour to the left
        cellRight = [0, 0]  # initialize the cell neighbour to the right
        cellBelow = [0, 0]  # initialize the cell neighbour directly below
        cellAbove = [0, 0]  # initialize the cell neighbour directly above

        # cell left if cell(x) != 0
        # what unreadable claptrap .... but it works
        if cell[2][1] != self.boundary["lower"]:
            if self.square[cell[2][0]][cell[2][1] - 1][0] == 'x' and self.square[cell[2][0]][cell[2][1] - 1][1] == 0:
                adjacentCells.append(self.square[cell[2][0]][cell[2][1] - 1])
                self.square[cell[2][0]][cell[2][1] - 1][1] = cell[1]

        # cell right if cell(x) != upper boundary
        if cell[2][1] != self.boundary["upper"]:
            cellRight = self.square[cell[2][0]][cell[2][1] + 1]

        # cell beneath if cell(y) != upper boundary
        if cell[2][0] != self.boundary["upper"]:
            cellBelow = self.square[cell[2][0] + 1][cell[2][1]]

        # cell above if cell(y) != lower boundary
        if cell[2][0] != self.boundary["lower"]:
            cellAbove = self.square[cell[2][0] - 1][cell[2][1]]

        # 'x' indicates the cell to the LEFT is neighbour, '0' indicates it is not CURRENTLY part of an island
        # if cellLeft[0] == 'x' and cellLeft[1] == 0:
        #     # append this cell to list for recursion
        #     adjacentCells.append(cellLeft)
        #     # give the neighbouring cell the same island num as the reference cell. Now part of an island!
        #     cellLeft[1] = cell[1]

        if cellRight[0] == 'x' and cellRight[1] == 0:
            adjacentCells.append(cellRight)
            cellRight[1] = cell[1]

        if cellBelow[0] == 'x' and cellBelow[1] == 0:
            adjacentCells.append(cellBelow)
            cellBelow[1] = cell[1]

        if cellAbove[0] == 'x' and cellAbove[1] == 0:
            adjacentCells.append(cellAbove)
            cellAbove[1] = cell[1]

        # this loop is essentially implements a depth-first search (DFS) tree traversal
        if len(adjacentCells) != 0:
            for aCell in adjacentCells:
                self.xNeighbor(aCell)  # <---- recursion
                self.recursionLoops += 1

    # how many islands did we find?
    def getNumIslands(self):
        print("number of islands = " + str(self.islandNum) + " [" + str(self.recursionLoops) + " loops]")


testingRecursion = TestingRecursion()

testingRecursion.iterateSquare()

# testingRecursion.printSquare()

testingRecursion.prettyPrintSquare()

testingRecursion.getNumIslands()
