import pygame

from levels.mainlevel import MainLevel
from config.config import *

class Game:

    def __init__(self):
        pygame.init()
        self.setup()

    def setup(self):
        # Set up window
        pygame.display.set_caption("Pygame Template")
        self.screen = pygame.display.set_mode(( WIDTH, HEIGHT ))
        self.time = pygame.time.Clock()

        self.main = MainLevel()

    def run(self):

        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update screen
            pygame.display.update()
            pygame.display.flip()
            
            # Fill background with white
            self.screen.fill("white")
            
            # Update sprites
            self.main.update()

            # FPS limit to 60
            self.time.tick(60)

        pygame.quit()



if __name__ == '__main__':
    g = Game()
    g.run()