import pygame
from pygame.sprite import Sprite


class PowerPellet(Sprite):

    def __init__(self, screen):
        super(PowerPellet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/Power_Pellet.png')
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect()

    def update(self):
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
