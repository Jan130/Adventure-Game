import Parser
import Weapon
import pygame
import random
import os

#jobs:
#1: knight
#2: archer
#3: magician

class Player:
    def __init__(self, name, health, level, weapon, job, pos, image, mode = "auto"):
        self.name = name
        self.health = health
        self.level = level
        self.weapon = weapon
        self.job = job
        self.pos = pos
        self.radius = 20
        self.color = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
        self.speed = 5
        self.alive = True
        self.mode = mode
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Graphics", image)), (40, 40))

    def attack(self, player, filename):
        if pygame.math.Vector2.distance_to(pygame.math.Vector2(self.pos), pygame.math.Vector2(player.pos)) <= Parser.get_range(filename, self.job) and player is not self and player.alive:
            player.health -= self.weapon.damage
            print(self.name + "(" + str(self.health) + ")" + " --" + str(self.weapon.damage) + "-> " + player.name + "(" + str(player.health) + ")")

    def render(self, screen):
        #pygame.draw.circle(screen, self.color, self.pos, self.radius)
        screen.blit(self.image, self.pos)

    def handleKey(self, key, keys, players, filename = 'config.yml'):
        if self.alive:
            if key is getattr(pygame, keys["up"]):
                self.move("U", filename)
            if key is getattr(pygame, keys["down"]):
                self.move("D", filename)
            if key is getattr(pygame, keys["left"]):
                self.move("L", filename)
            if key is getattr(pygame, keys["right"]):
                self.move("R", filename)
            if key is getattr(pygame, keys["attack"]):
                for pl in players:
                    self.attack(pl, filename)

    def move(self, direction, filename):
        if direction is "U":
            if (self.pos[1] - self.speed) >= 0:
                self.pos[1] -= self.speed
        if direction is "D":
            if (self.pos[1] + self.speed) <= Parser.get_screen_height(filename):
                self.pos[1] += self.speed
        if direction is "L":
            if (self.pos[0] - self.speed) >= 0:
                self.pos[0] -= self.speed
        if direction is "R":
            if (self.pos[0] + self.speed) <= Parser.get_screen_width(filename):
                self.pos[0] += self.speed

    def die(self):
        self.alive = False

    def update(self, screen, players, filename = "config.yml"):
        if self.alive:
            if self.health <= 0:
                self.die()
            self.render(screen)
        if self.mode == "auto":
            for pl in players:
                self.attack(pl, filename)

class Knight(Player):
    def __init__(self, filename, name, pos, mode = "auto"):
        super().__init__(name, Parser.get_health(filename, "Knight"), 1, Weapon.Sword(Parser.get_weapon_name(filename, "Knight", 1), Parser.get_weapon_damage(filename, "Knight", 1)), "Knight", pos, Parser.get_image(filename, "Knight"), mode)

class Archer(Player):
    def __init__(self, filename, name, pos, mode = "auto"):
        super().__init__(name, Parser.get_health(filename, "Archer"), 1, Weapon.Bow(Parser.get_weapon_name(filename, "Archer", 1), Parser.get_weapon_damage(filename, "Archer", 1)), "Archer", pos, Parser.get_image(filename, "Archer"), mode)

class Magician(Player):
    def __init__(self, filename, name, pos, mode = "auto"):
        super().__init__(name, Parser.get_health(filename, "Magician"), 1, Weapon.Wand(Parser.get_weapon_name(filename, "Magician", 1), Parser.get_weapon_damage(filename, "Magician", 1)), "Magician", pos, Parser.get_image(filename, "Magician"), mode)
        print("Magician initialized!")
