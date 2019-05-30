class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Sword(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Bow(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Wand(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
