import Player
import pygame

config = "config.yml"

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Adventure Game")
    pygame.mouse.set_visible(1)
    screen.fill((255, 255, 255))

    player = Player.Archer(config, "Test Archer", [400, 300])

    running = True
    while running:

        player.render(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        pygame.display.flip()




if __name__ == "__main__":
    main()
