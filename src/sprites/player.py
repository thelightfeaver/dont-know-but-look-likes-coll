"""This module contains the player class."""


import time

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
        self.speed = 10
        
        # bullet cooldown
        self.bulllet_cooldown = time.time()
        self.ready_to_shoot = True


    def _recharge_shoot(self):
        if time.time() - self.bulllet_cooldown > 0.1:
            self.bulllet_cooldown = time.time()
            self.ready_to_shoot = True

    def _move(self):

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
        self._move()
        self._recharge_shoot()