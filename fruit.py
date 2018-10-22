import pygame
from pygame.sprite import Sprite


class Fruit(Sprite):

    def __init__(self, game_master):
        super(Fruit, self).__init__()
        self.game_master = game_master
        self.screen = game_master.screen
        self.image = pygame.image.load('images/Fruit_Cherry.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()

    def update(self):
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
