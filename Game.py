import Player
import pygame

config = "config.yml"

def main():
    player = Player.Knight(config, "King Arthur", (0, 0))
    player2 = Player.Archer(config, "Robin Hood", (10, 10))

    player.attack(player2)
    print(player2.health)


if __name__ == "__main__":
    main()
