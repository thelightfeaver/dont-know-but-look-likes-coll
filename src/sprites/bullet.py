import pygame

class Bullet(pygame.sprite.Sprite):


    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
    
    def _move(self):
        self.rect.move_ip(0, -1 * self.speed)

    def _outside_screen(self):
        if self.rect.y < 0:
            self.kill()

    def update(self):
        self._move()
        self._outside_screen()
    
