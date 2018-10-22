import pygame
from pygame.sprite import Sprite


class Pellet(Sprite):

    def __init__(self, screen):
        super(Pellet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/Pellet.png')
        self.image = pygame.transform.scale(self.image, (6, 6))
        self.rect = self.image.get_rect()

    def update(self):
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
