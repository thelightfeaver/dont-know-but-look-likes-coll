"""This module contains the player class."""

import pygame

class Player(pygame.sprite.Sprite):


    def __init__(self, x, y):
        super().__init__()
        
        # Create a surface and fill it with red
        self.image = pygame.Surface((30, 30))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Set speed
        self.speed = 5
        
        # bullet cooldown
        self.bulllet_cooldown = 100
        self.ready_to_shoot = True


    def _recharge(self):
        if not self.ready_to_shoot:
            self.bulllet_cooldown -= 1
            if self.bulllet_cooldown <= 0:
                self.ready_to_shoot = True
                self.bulllet_cooldown = 100

    def _move(self):

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
        self._move()
        self._recharge()