import pygame
from intro_animation import IntroAnimation


class IntroGameMaster:

    def __init__(self, player_input, settings, screen):
        self.settings = settings
        self.screen = screen
        self.player_input = player_input

        self.logo_image = pygame.image.load('images/Pacman_logo.png')
        self.logo_image_rect = self.logo_image.get_rect()
        self.logo_image_rect.center = (self.settings.screen_width * 0.5, (self.settings.screen_height * 0.5) - 250)

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)

        self.play_text_image = self.font.render("PRESS ENTER!", True, self.text_color, (0, 0, 0))
        self.play_text_image_rect = self.play_text_image.get_rect()
        self.play_text_image_rect.center = (self.settings.screen_width * 0.5, (self.settings.screen_height * 0.5) + 250)

        f = open("Highscores.txt", "r")
        self.highscore_text = f.read()
        if self.highscore_text == '':
            self.highscore_text = '0'
        f.close()
        self.highscore_text_image = self.font.render(
            "Highscore: " + self.highscore_text, True, self.text_color, (0, 0, 0)
        )
        self.highscore_rect = self.highscore_text_image.get_rect()
        self.highscore_rect.center = (self.settings.screen_width * 0.5, (self.settings.screen_height * 0.5) + 300)

        self.intro_animation = IntroAnimation(self)

    def update(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.play_text_image, self.play_text_image_rect)
        self.screen.blit(self.highscore_text_image, self.highscore_rect)
        self.screen.blit(self.logo_image, self.logo_image_rect)
        self.intro_animation.update()
