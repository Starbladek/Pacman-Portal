import pygame
from pygame.sprite import Sprite


class GhostInky(Sprite):

    def __init__(self, game_master):
        super(GhostInky, self).__init__()
        self.screen = game_master.screen
        self.screen_rect = self.screen.get_rect()

        self.normal_image = pygame.image.load('images/Inky_Right.png')
        self.normal_image = pygame.transform.scale(self.normal_image, (24, 24))
        self.fear_image_1 = pygame.image.load('images/Scared_1.png')
        self.fear_image_1 = pygame.transform.scale(self.fear_image_1, (24, 24))
        self.fear_image_2 = pygame.image.load('images/Scared_2.png')
        self.fear_image_2 = pygame.transform.scale(self.fear_image_2, (24, 24))

        self.current_image = self.normal_image
        self.rect = self.current_image.get_rect()

        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_time = 0

        self.fear = False
        self.fear_timer = 0
        self.fear_flashing = False
        self.fear_flash_timer = 0

    def update(self):
        self.delta_time = pygame.time.get_ticks() - self.last_frame_ticks
        self.last_frame_ticks = pygame.time.get_ticks()

        if self.fear:
            self.fear_timer -= self.delta_time

            if self.fear_timer < 3000 and not self.fear_flashing:
                self.fear_flashing = True
                self.fear_flash_timer = 250
                self.current_image = self.fear_image_2

            if self.fear_flashing:
                self.fear_flash_timer -= self.delta_time
                if self.fear_flash_timer <= 0:
                    self.fear_flash_timer = 250
                    if self.current_image == self.fear_image_1:
                        self.current_image = self.fear_image_2
                    else:
                        self.current_image = self.fear_image_1

            if self.fear_timer <= 0:
                self.fear = False
                self.fear_flashing = False
                self.fear_timer = 0
                self.fear_flash_timer = 0
                self.current_image = self.normal_image

        self.blitme()

    def blitme(self):
        self.screen.blit(self.current_image, self.rect)

    def induce_fear(self):
        self.fear = True
        self.fear_timer = 8000
        self.current_image = self.fear_image_1
