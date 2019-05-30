import Parser
import Weapon

#jobs:
#1: knight
#2: archer
#3: magician

class Player:
    def __init__(self, name, health, level, weapon):
        self.name = name
        self.health = health
        self.level = level
        self.weapon = weapon

class Knight(Player):
    def __init__(self, filename, name):
        super().__init__(name, Parser.get_health(filename, "Knight"), 1, Weapon.Sword("Basic Sword"))

class Archer(Player):
    def __init__(self, filename, name):
        super().__init__(name, Parser.get_health(filename, "Archer"), 1, Weapon.Bow("Basic Bow"))

class Magician(Player):
    def __init__(self, filename, name):
        super().__init__(name, Parser.get_health(filename, "Magician"), 1, Weapon.Wand("Basic Wand"))
