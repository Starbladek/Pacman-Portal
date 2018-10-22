import pygame
from pygame.sprite import Sprite


class WallBlock(Sprite):

    def __init__(self, game_master):
        super(WallBlock, self).__init__()
        self.screen = game_master.screen
        self.image = pygame.image.load('images/Wall square.png')
        self.image = pygame.transform.scale(
            self.image,
            (game_master.settings.wall_block_scale, game_master.settings.wall_block_scale)
        )
        self.rect = self.image.get_rect()

    def update(self):
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
