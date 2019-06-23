import Player
import pygame
import Parser

config = "config.yml"

def main():
    pygame.init()
    screen = pygame.display.set_mode((Parser.get_screen_width(config), Parser.get_screen_height(config)))
    pygame.display.set_caption("Adventure Game")
    pygame.mouse.set_visible(1)
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 30)

    player = Player.Archer(config, "Test Archer", [400, 300])
    player2 = Player.Knight(config, "Test Knight", [100, 100])

    players = [player, player2]



    keys = Parser.get_keys(config)

    running = True
    while running:

        clock.tick(30)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                else:
                    players[0].handleKey(event.key, keys)



        screen.fill((255, 255, 255))

        for pl in players:
            pl.update(screen)

        pygame.display.flip()




if __name__ == "__main__":
    main()
