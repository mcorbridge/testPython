#!/usr/bin/python3

class Family:
    def __init__(self):
        print("Calling FAMILY constructor")

    def setAttr(self, attr):
        Family.lastName = attr

    def getAttr(self):
        print("FAMILY last name:", Family.lastName)

    def setLastNameMethod(self, lastName):
        Family.setAttr(self, lastName)

    def getLastNameMethod(self):
        Family.getAttr(self)

class Parent(Family):        # define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling PARENT constructor")

    def parentMethod(self):
        print ('Calling PARENT method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("PARENT attribute :", Parent.parentAttr)

class Child(Parent): # define child class
    def __init__(self):
        print ("Calling CHILD constructor")

    def childMethod(self):
        print ('Calling CHILD method')



c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.setLastNameMethod('Foo') # call 'Family' setter
c.getLastNameMethod()   # call 'Family' getter
