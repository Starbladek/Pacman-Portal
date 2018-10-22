import pygame


class IntroAnimation:

    def __init__(self, intro_game_master):
        self.intro_game_master = intro_game_master
        self.screen = self.intro_game_master.screen
        self.screen_width = self.intro_game_master.settings.screen_width
        self.screen_height = self.intro_game_master.settings.screen_height

        self.phase = 0

        self.frame_timer = self.intro_game_master.settings.pacman_animation_frame_length
        self.frame_counter = 0

        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_time = 0

        self.pacman_images = [
            pygame.image.load('images/Pacman1.png'),
            pygame.image.load('images/Pacman2.png'),
            pygame.image.load('images/Pacman3.png'),
            pygame.image.load('images/Pacman4.png')
        ]

        self.pacman_images[0] = pygame.transform.scale(self.pacman_images[0], (48, 48))
        self.pacman_images[1] = pygame.transform.scale(self.pacman_images[1], (48, 48))
        self.pacman_images[2] = pygame.transform.scale(self.pacman_images[2], (48, 48))
        self.pacman_images[3] = pygame.transform.scale(self.pacman_images[3], (48, 48))

        self.current_pacman_image = self.pacman_images[0]
        self.pacman_rect = self.current_pacman_image.get_rect()
        self.pacman_rect.center = (
            self.screen_width + 200,
            self.screen_height * 0.5
        )

        self.blinky_image = pygame.image.load('images/Blinky_Right.png')
        self.blinky_image = pygame.transform.scale(self.blinky_image, (48, 48))
        self.blinky_rect = self.blinky_image.get_rect()
        self.blinky_rect.center = (-200, self.screen_height * 0.5)

        self.pinky_image = pygame.image.load('images/Pinky_Right.png')
        self.pinky_image = pygame.transform.scale(self.pinky_image, (48, 48))
        self.pinky_rect = self.pinky_image.get_rect()
        self.pinky_rect.center = (-200, self.screen_height * 0.5)

        self.inky_image = pygame.image.load('images/Inky_Right.png')
        self.inky_image = pygame.transform.scale(self.inky_image, (48, 48))
        self.inky_rect = self.inky_image.get_rect()
        self.inky_rect.center = (-200, self.screen_height * 0.5)

        self.clyde_image = pygame.image.load('images/Clyde_Right.png')
        self.clyde_image = pygame.transform.scale(self.clyde_image, (48, 48))
        self.clyde_rect = self.clyde_image.get_rect()
        self.clyde_rect.center = (-200, self.screen_height * 0.5)

        self.scared_image = pygame.image.load('images/Scared_1.png')
        self.scared_image = pygame.transform.scale(self.scared_image, (48, 48))
        self.scared_rect = self.scared_image.get_rect()
        self.scared_rect.center = (-200, self.screen_height * 0.5)

    def update(self):
        self.delta_time = pygame.time.get_ticks() - self.last_frame_ticks
        self.last_frame_ticks = pygame.time.get_ticks()

        self.frame_timer -= self.delta_time
        if self.frame_timer <= 0:
            self.frame_timer += self.intro_game_master.settings.pacman_animation_frame_length
            self.frame_counter += 1
            if self.frame_counter > len(self.pacman_images) - 1:
                self.frame_counter = 0
            self.current_pacman_image = self.pacman_images[self.frame_counter]

        # Pacman moving by himself
        if self.phase == 0:
            self.pacman_rect.centerx -= 1

            if self.pacman_rect.centerx < -500:
                self.pacman_rect.centerx = -50
                self.phase = 1

        # Pacman being chased by ghosts
        elif self.phase == 1:
            self.pacman_rect.centerx += 1
            self.blinky_rect.centerx = self.pacman_rect.centerx - 75
            self.pinky_rect.centerx = self.pacman_rect.centerx - 150
            self.inky_rect.centerx = self.pacman_rect.centerx - 225
            self.clyde_rect.centerx = self.pacman_rect.centerx - 300

            if self.pacman_rect.centerx > self.screen_width + 600:
                self.pacman_rect.centerx = self.screen_width + 600
                self.phase = 2

        # Pacman chasing ghrosts
        elif self.phase == 2:
            self.pacman_rect.centerx -= 1
            self.blinky_rect.centerx = self.pacman_rect.centerx - 75
            self.pinky_rect.centerx = self.pacman_rect.centerx - 150
            self.inky_rect.centerx = self.pacman_rect.centerx - 225
            self.clyde_rect.centerx = self.pacman_rect.centerx - 300

            if self.pacman_rect.centerx < -500:
                self.pacman_rect.centerx = self.screen_width + 600
                self.phase = 0

        self.blitme()

    def blitme(self):
        if self.phase == 0 or self.phase == 2:
            self.screen.blit(self.current_pacman_image, self.pacman_rect)
            self.screen.blit(self.scared_image, self.blinky_rect)
            self.screen.blit(self.scared_image, self.pinky_rect)
            self.screen.blit(self.scared_image, self.inky_rect)
            self.screen.blit(self.scared_image, self.clyde_rect)
        else:
            self.screen.blit(pygame.transform.rotate(self.current_pacman_image, 180), self.pacman_rect)
            self.screen.blit(self.blinky_image, self.blinky_rect)
            self.screen.blit(self.pinky_image, self.pinky_rect)
            self.screen.blit(self.inky_image, self.inky_rect)
            self.screen.blit(self.clyde_image, self.clyde_rect)
