class BuiltIns:

    def __init__(self):
        print("BuiltIns constructor")

    @staticmethod
    def testBuiltIns():
        print("********************************************************************")

        print(abs(-1))

        allTrue = (True, True, True, True, True, True, True)
        mostTrue = (True, True, False, True, True, True, True)
        allFalse = (False, False, False, False, False, False, False)

        print(all(allTrue))
        print(all(mostTrue))

        print(any(allTrue))
        print(any(allFalse))

        print(ascii("https:\\docs.python.org/3/library/functions.html#any"))

        print(bin(2019))

        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        print(list(enumerate(seasons)))

        # list of alphabets
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u',
                     'v', 'w', 'x', 'y', 'z']

        zalphabets = [('a', 1, 'foo', True), ('b', 2, 'bar', True), ('d', 3, 'qqq', False), ('e', 4, 'uwe', True)]
        balphabets = [('z', 1), ('y', 2), ('x', 3), ('w', 4)]

        # function that filters vowels
        def filterVowels(zalphabets):
            vowels = ['a', 'e', 'i', 'o', 'u', 'y']

            if (zalphabets[0] in vowels):
                return True
            else:
                return False

        def filterBool(zalphabets):
            if(zalphabets[3]):
                return True
            else:
                return False

        filteredVowels = filter(filterVowels, zalphabets)

        print('The filtered vowels are:')
        for vowel in filteredVowels:
            print(vowel)

        filteredBools = filter(filterBool, zalphabets)

        print('The boolean items are:')
        for bool in filteredBools:
            print(bool)

        print("888888888888888888888888888888888888888888888888888888888888888888888")

        row1 = ([1, 1, 'o', 0], [1, 2, 'o', 0], [1, 3, 'o', 0], [1, 4, 'o', 0], [1, 5, 'o', 0])
        row2 = ([2, 1, 'x', 0], [2, 2, 'x', 0], [2, 3, 'o', 0], [2, 4, 'o', 0], [2, 5, 'o', 0])
        row3 = ([3, 1, 'x', 0], [3, 2, 'x', 0], [3, 3, 'o', 0], [3, 4, 'o', 0], [3, 5, 'o', 0])
        row4 = ([4, 1, 'o', 0], [4, 2, 'o', 0], [4, 3, 'o', 0], [4, 4, 'o', 0], [4, 5, 'o', 0])
        row5 = ([5, 1, 'o', 0], [5, 2, 'o', 0], [5, 3, 'o', 0], [5, 4, 'o', 0], [5, 5, 'o', 0])

        square = (row1, row2, row3, row4, row5)

        def filterRow(row):
            if(row[2] == 'x'):
                return True
            else:
                return False

        def filterSquare(square):
            if filter(filterRow,square) == True:
                return False
            else:
                return True

        filteredSquare = (filterSquare, square)

        filteredRows1 = filter(filterRow, row1)
        filteredRows2 = filter(filterRow, row2)
        filteredRows3 = filter(filterRow, row3)
        filteredRows4 = filter(filterRow, row4)
        filteredRows5 = filter(filterRow, row5)

        xCells = list()

        for row in filteredRows1:
            xCells.append(row)
        for row in filteredRows2:
            xCells.append(row)
        for row in filteredRows3:
            xCells.append(row)
        for row in filteredRows4:
            xCells.append(row)
        for row in filteredRows5:
            xCells.append(row)

        print(xCells)

        print("-----------------------------------------------------------------------------------------------")
        print("q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q")
        print("-----------------------------------------------------------------------------------------------")

        for row in filteredSquare:
            print(row)

        print(id(filteredSquare))
        print(type(filteredSquare))
        print(dir(filteredSquare))

        lidy = ('a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v')
        nidy = (0,100,9,23,76,67,1,23,8,9,0,100,9,23,76,67,1,23,8,9,0,100,9,23,76,67,1,23,8,9,0,100,9,23,76,67,1,23,8,9,0,100,9,23,76,67,1,23,8,9,0,100,9,23,76,67,1,23,8,9,)

        sortedLidy = sorted(lidy)
        sortedNidy = sorted(nidy)

        print(sortedLidy)
        print(sortedNidy)

        print(sum(nidy))

        a = ("John", "Charles", "Mike")
        b = ("Smith", "Warren", "Gabooboo")
        c = (4, 3, 1)
        d = ([123,'eed'], [324,'qse'], [142,'dsq'], [999,'xxx'])

        x = zip(a, b, c, d)

        for i in x:
            print(i)
            print(i[3])
            print(i[3][0])

        # Python program to illustrate
        # Modifying internal data using memory view

        # random bytearray
        byte_array = bytearray('XYZ', 'utf-8')
        print('Before update:', byte_array)

        mem_view = memoryview(byte_array)

        # update 2nd index of mem_view to J
        mem_view[2] = 74
        print('After update:', byte_array)




BuiltIns.testBuiltIns()
