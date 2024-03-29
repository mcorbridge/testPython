# Factory/Games.py
# An example of the Abstract Factory pattern.

class Obstacle:
    def action(self): pass

class Character:
    def interactWith(self, obstacle): pass


class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a", obstacle.action())

class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a", obstacle.action())

class KayakingGuy(Character):
    def interactWith(self, obstacle):
        print("We are now kayaking the Sound in a ", obstacle.action())

class Puzzle(Obstacle):
    def action(self):
        print("Puzzle")

class NastyWeapon(Obstacle):
    def action(self):
        print("NastyWeapon")

class Looksha(Obstacle):
    def action(self):
        print("Necky Kayak")

# The Abstract Factory:
class GameElementFactory:
    def makeCharacter(self): pass
    def makeObstacle(self): pass


# Concrete factories:
class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()


class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastyWeapon()


class GoKayaking(GameElementFactory):
    def makeCharacter(self): return KayakingGuy()
    def makeObstacle(self): return Looksha()


class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()

    def play(self):
        self.p.interactWith(self.ob)


g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g3 = GameEnvironment(GoKayaking())

g1.play()
g2.play()
g3.play()
