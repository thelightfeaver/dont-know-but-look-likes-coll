import random, time

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

        # lol
        self.generation_enemy_time = time.time()
        self.pause = False
        self.limit_wave = len(WAVES) 
        self.index_wave = 0

        # Load Map
        self.create_maps()

    def create_maps(self):
        self.blocks.add(Block(0, HEIGHT - 50, WIDTH, 10))

    def update(self):

        if not self.pause:
            self._draw()
            self._handle_events()
            self._check_collisions()
            self._generation_enemy()

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
        print(f"Time: {time.time() - self.generation_enemy_time}")
        print(f"Index: {self.index_wave}")

        if self.index_wave < self.limit_wave:
           
            if time.time() - self.generation_enemy_time > int(WAVES[self.index_wave]["time"]):
                for _ in range(WAVES[self.index_wave]["enemies"]):
                    self.generation_enemy_time = time.time()
                    self.enemies.add(Enemy(random.randint(50, WIDTH - 50), 10))
                self.index_wave += 1

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