import pygame
from pygame.sprite import Group
from fruit import Fruit


class FruitSpawner:

    def __init__(self, game_master):
        self.game_master = game_master

        self.fruits = Group()
        self.fruit_spawn_position_x = 0
        self.fruit_spawn_position_y = 0

        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_time = 0

        self.spawn_timer = 10000

    def update(self):
        self.delta_time = pygame.time.get_ticks() - self.last_frame_ticks
        self.last_frame_ticks = pygame.time.get_ticks()
        self.spawn_timer -= self.delta_time
        if self.spawn_timer <= 0:
            self.spawn_timer = 10000
            if len(self.fruits) == 0:
                fruit = Fruit(self.game_master)
                fruit.rect.center = (self.fruit_spawn_position_x, self.fruit_spawn_position_y)
                self.fruits.add(fruit)
        for fruit in self.fruits:
            fruit.update()
