import Parser

#jobs:
#1: knight
#2: archer
#3: magician

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = 100

class Knight(Player):
    def __init__(self, filename, name):
        super().__init__(name, Parser.get_health(filename, "Knight"))

class Archer(Player):
    def __init__(self, filename, name):
        super().__init__(name, Parser.get_health(filename, "Archer"))

class Magician(Player):
    def __init__(self, filename, name):
        super().__init__(name, Parser.get_health(filename, "Magician"))
