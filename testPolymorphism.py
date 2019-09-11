class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")

class ElectricEel:
    def wiggle(self):
        print("The Electiric Eel is slithering through the muddy water.")

    def wiggle_backwards(self):
        print("The Electiric Eel cannot wiggle backwards.")

    def structure(self):
        print("The Electiric Eel's skeleton is long and skinny.")

sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()

shocky = ElectricEel()
shocky.structure()


for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()

print("=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=")

class Abstract:
  def myFunc(self):
      raise NotImplementedError("The method not implemented")

class NewKlass(Abstract):
    def __init__(self):
        print("class constructor")

    def myFunc(self):
        print("myFunc method")

abstract = Abstract()
newKlass = NewKlass()