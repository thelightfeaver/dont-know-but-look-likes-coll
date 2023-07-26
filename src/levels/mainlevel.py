import random

import pygame

from sprites.player import Player
from sprites.block import Block
from sprites.bullet import Bullet
from sprites.enemy import Enemy
from config.config import *

class MainLevel:

    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.player = pygame.sprite.GroupSingle(Player(WIDTH // 2, HEIGHT -20 ))
        self.blocks = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.create_maps()
        self._generation_enemy()

    def create_maps(self):
        self.blocks.add(Block(0, HEIGHT - 50, WIDTH, 10))

    def update(self):
        self._draw()
        self._handle_events()
        self._check_collisions()

    def _draw(self):
        self.player.draw(self.surface)
        self.player.update()
        self.blocks.draw(self.surface)
        self.blocks.update()
        self.bullets.draw(self.surface)
        self.bullets.update()
        self.enemies.draw(self.surface)
        self.enemies.update()

    def _generation_enemy(self):
        self.enemies.add(Enemy(random.randint(50, 250), 10))

    def _check_collisions(self):
        # collision between enemy and bullets
        for enemy in self.enemies:
            if pygame.sprite.spritecollide(enemy, self.bullets, True):
                enemy.get_damage(10)

    def _handle_events(self):
        
        # IF pressed space, shoot

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.player.sprite.ready_to_shoot:
                self.player.sprite.ready_to_shoot = False
                self.bullets.add(Bullet(self.player.sprite.rect.center[0], self.player.sprite.rect.center[1]))