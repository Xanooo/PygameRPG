import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("PyPokemon")
        self.clock = pygame.time.Clock()
        self.running = True
        self.framerate = 60

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.screen.fill((0, 0, 0))


