import Player

class Weapon:
    def __init__(self, name, damage, ownerJob):
        self.name = name
        self.damage = damage
        self.ownerJob = ownerJob

class Sword(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage, Player.Knight)

class Bow(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage, Player.Archer)

class Wand(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage, Player.Magician)
