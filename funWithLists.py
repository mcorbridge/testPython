import copy

class FunWithLists:

    print("-----------------------------------")
    foo = "foo"
    print("| print foo >>>>> foo " + foo + "         |")
    print("-----------------------------------")

    def __init__(self):
        print("FUN WITH PYTHON LISTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        self.capeCodTowns = ['Bourne', 'Falmouth', 'Sandwich', 'Mashpee', 'Barnstable', 'Yarmouth', 'Brewster', 'Harwich',
                    'Chatham', 'Orleans', 'Eastham', 'Wellfleet', 'Truro', 'Provincetown']

        self.capeCodTownsClone = copy.copy(self.capeCodTowns)

        self.x = 1


    def listCapeCodTowns(self):
        global capeCodTowns
        print(self.capeCodTowns)

    def testPop(self):
        return self.capeCodTowns.pop()

    def listAppend(self,capeCodTowns):
        for town in capeCodTowns:
            self.capeCodTowns.append(town)

    def sortCapeCodTowns(self):
        print(sorted(self.capeCodTowns))

    def listClone(self):
        print(self.capeCodTownsClone)

    def testClone(self):
        l0 = [1,[1,2,3],2,(1,2,[3,4,5])]
        cl = copy.copy(l0)
        print(cl)
        c2 = copy.deepcopy(l0)
        print(c2)

    def testRemove(self,town):
        self.capeCodTowns.remove(town)
        print(self.capeCodTowns)

    def testInsert(self,pos,town):
        self.capeCodTowns.insert(pos,town)
        print(self.capeCodTowns)

    def testTernary(self,arg):
        return arg if (arg > 100) else 100



    def testRFunc(self):
        y = 'yr'
        def rFunc():
            print("rFunc >>>>>> " + str(self.x) + " " + y)
        return rFunc

    def printFoo(self):
        print("printFoo >>>>> self.foo " + self.foo)


funWithLists = FunWithLists()
funWithLists.listCapeCodTowns()
a = funWithLists.testPop()
print("pop " + a + "!")
funWithLists.listCapeCodTowns()
b = funWithLists.testPop()
print("pop " + b + "!")
funWithLists.listCapeCodTowns()
c = funWithLists.testPop()
print("pop " + c + "!")
funWithLists.listCapeCodTowns()
d = funWithLists.testPop()
print("pop " + d + "!")
funWithLists.listCapeCodTowns()
e = funWithLists.testPop()
print("pop " + e + "!")
funWithLists.listCapeCodTowns()
f = funWithLists.testPop()
print("pop " + f + "!")
funWithLists.listCapeCodTowns()
g = funWithLists.testPop()
print("pop " + g + "!")
funWithLists.listCapeCodTowns()
h = funWithLists.testPop()
print("pop " + h + "!")
funWithLists.listCapeCodTowns()
i = funWithLists.testPop()
print("pop " + i + "!")
funWithLists.listCapeCodTowns()
j = funWithLists.testPop()
print("pop " + j + "!")
funWithLists.listCapeCodTowns()
k = funWithLists.testPop()
print("pop " + k + "!")
funWithLists.listCapeCodTowns()
l = funWithLists.testPop()
print("pop " + l + "!")
funWithLists.listCapeCodTowns()
m = funWithLists.testPop()
print("pop " + m + "!")
funWithLists.listCapeCodTowns()
n = funWithLists.testPop()
print("pop " + n + "!")
funWithLists.listCapeCodTowns()

funWithLists.listAppend([a,b,c,d,e,f,g,h,i,j,k,l,m,n])

funWithLists.listCapeCodTowns()

funWithLists.sortCapeCodTowns()

funWithLists.listClone()

funWithLists.testClone()

funWithLists.testRemove('Mashpee')

funWithLists.testInsert(0,'Mashpee')

print(funWithLists.testTernary(99))

print(funWithLists.testTernary(101))

r = funWithLists.testRFunc()
r()

funWithLists.printFoo()