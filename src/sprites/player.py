"""This module contains the player class."""

import pygame

class Player(pygame.sprite.Sprite):


    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5


    def _move(self):

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
        self._move()
    