import pygame.font


class Scoreboard:
    def __init__(self, game_master):
        self.game_master = game_master
        self.screen = game_master.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game_master.settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)

        self.score = 0
        self.score_image = None
        self.score_rect = None

        self.level = 1
        self.level_image = None
        self.level_rect = None

        f = open("Highscores.txt", "r")
        self.highscore = f.read()
        if self.highscore == '':
            self.highscore = 0
        else:
            self.highscore = int(self.highscore)
        f.close()
        self.highscore_image = None
        self.highscore_rect = None

        self.update_score_text()
        self.update_level_text()
        self.update_highscore_text()

    def update_score_text(self):
        rounded_score = int(round(self.score, -1))
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def update_level_text(self):
        self.level_image = self.font.render(str(self.level), True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.width * 0.5
        self.level_rect.top = 20

    def update_highscore_text(self):
        rounded_score = int(round(self.highscore, -1))
        score_str = "Highscore: {:,}".format(rounded_score)
        self.highscore_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.left = self.screen_rect.left + 20
        self.highscore_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
