import Parser
import Weapon
import pygame

#jobs:
#1: knight
#2: archer
#3: magician

class Player:
    def __init__(self, name, health, level, weapon, job, pos):
        self.name = name
        self.health = health
        self.level = level
        self.weapon = weapon
        self.job = job
        self.pos = pygame.math.Vector2(pos)

    def attack(self, player):
        if pygame.math.Vector2.distance_to(self.pos, player.pos) <= 20:
            player.health -= self.weapon.damage
            print(self.name + "(" + str(self.health) + ")" + " --" + str(self.weapon.damage) + "-> " + player.name + "(" + str(player.health) + ")")

class Knight(Player):
    def __init__(self, filename, name, pos):
        super().__init__(name, Parser.get_health(filename, "Knight"), 1, Weapon.Sword(Parser.get_weapon_name(filename, "Knight", 1), Parser.get_weapon_damage(filename, "Knight", 1)), "Knight", pos)

class Archer(Player):
    def __init__(self, filename, name, pos):
        super().__init__(name, Parser.get_health(filename, "Archer"), 1, Weapon.Bow(Parser.get_weapon_name(filename, "Archer", 1), Parser.get_weapon_damage(filename, "Archer", 1)), "Archer", pos)

class Magician(Player):
    def __init__(self, filename, name, pos):
        super().__init__(name, Parser.get_health(filename, "Magician"), 1, Weapon.Wand(Parser.get_weapon_name(filename, "Magician", 1), Parser.get_weapon_damage(filename, "Magician", 1)), "Magician", pos)
