

class TestListComprehension:

    def __init__(self):
        print("init TestListComprehension")

        x = [i for i in range(10)]
        print(x)

        squares = []

        for x in range(10):
            squares.append(x ** 2)

        print(squares)
        # list comprehension
        # a list resulting from evaluating the expression in the context of the 'for' and 'if' clauses which follow it.

        squares = [x ** 2 for x in range(10)]
        print(squares)

        squares = [x ** 2 for x in range(10) if (x ** 2 <= 45) and (x ** 2 >= 16)]
        print(squares)

        Wally = Pet("Wally")
        Wally.speak()
        Skinky = Pet("Skinky")
        Skinky.speak()



numPets = 0

class Pet(object):

    def __init__(self, name):
        global numPets
        self.name = name
        numPets += 1

    def speak(self):
        print("My name's "+ self.name + " and the number of pets is " + str(numPets))


testListComprehension = TestListComprehension()