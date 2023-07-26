"""This Module contains the enemy class."""

import random

import pygame

from config.config import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x ,  y) -> None:
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(5, 10)
        self._hp = 100

    def _move(self):
        self.rect.move_ip(0, 1 )

    def _outside_screen(self):
        if self.rect.y > HEIGHT - 80:
            self.rect.y = HEIGHT - 120

    def _check_hp(self):
        if self._hp <= 0:
            self.kill()

    def get_damage(self, damage):
        self._hp -= damage

    def update(self):
        self._move()
        self._outside_screen()
        self._check_hp()