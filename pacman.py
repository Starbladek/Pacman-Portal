import pygame
from pygame.sprite import Sprite


class Pacman(Sprite):

    def __init__(self, game_master):
        super(Pacman, self).__init__()
        self.game_master = game_master
        self.player_input = game_master.player_input
        self.settings = game_master.settings

        self.screen = game_master.screen
        self.screen_rect = self.screen.get_rect()

        self.speed = self.settings.pacman_speed
        self.spawn_position_x = 0
        self.spawn_position_y = 0
        self.extra_lives = 2
        self.dying = False
        self.end_game = False

        self.entrance_portal_image = pygame.image.load('images/Entrance_Portal.png')
        self.exit_portal_image = pygame.image.load('images/Exit_Portal.png')
        self.entrance_portal_rect = None
        self.exit_portal_rect = None
        self.portal_cooldown_timer = 0

        self.frame_timer = self.settings.pacman_animation_frame_length
        self.frame_counter = 0

        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_time = 0

        self.image_frames = [
            pygame.image.load('images/Pacman1.png'),
            pygame.image.load('images/Pacman2.png'),
            pygame.image.load('images/Pacman3.png'),
            pygame.image.load('images/Pacman4.png')
        ]

        for i in range(len(self.image_frames)):
            self.image_frames[i] = pygame.transform.scale(self.image_frames[i], (24, 24))

        self.current_image = self.image_frames[self.frame_counter]

        self.rect = self.current_image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

        self.previous_position = self.rect.center

        self.face_dir = 0

        self.death_frames = [
            pygame.image.load('images/Pacman_Death_1.png'),
            pygame.image.load('images/Pacman_Death_2.png'),
            pygame.image.load('images/Pacman_Death_3.png'),
            pygame.image.load('images/Pacman_Death_4.png'),
            pygame.image.load('images/Pacman_Death_5.png'),
            pygame.image.load('images/Pacman_Death_6.png'),
            pygame.image.load('images/Pacman_Death_7.png'),
            pygame.image.load('images/Pacman_Death_8.png'),
            pygame.image.load('images/Pacman_Death_9.png'),
            pygame.image.load('images/Pacman_Death_10.png')
        ]

        for i in range(len(self.death_frames)):
            self.death_frames[i] = pygame.transform.scale(self.death_frames[i], (24, 24))

        self.chomp_pellet_sound_1 = pygame.mixer.Sound('sounds/chomp_pellet_1.wav')
        self.chomp_pellet_sound_2 = pygame.mixer.Sound('sounds/chomp_pellet_2.wav')
        self.current_chomp_pellet_sound = 1

        self.chomp_fruit_sound = pygame.mixer.Sound('sounds/chomp_fruit.wav')
        self.power_pellet_tone_sound = pygame.mixer.Sound('sounds/power_pellet_tone.wav')
        self.death_sound = pygame.mixer.Sound('sounds/pacman_death.wav')

        self.fire_entrance_portal_sound = pygame.mixer.Sound('sounds/fire_entrance_portal.wav')
        self.fire_exit_portal_sound = pygame.mixer.Sound('sounds/fire_exit_portal.wav')
        self.travel_through_portal_sound = pygame.mixer.Sound('sounds/travel_through_portal.wav')

    def update(self):
        self.delta_time = pygame.time.get_ticks() - self.last_frame_ticks
        self.last_frame_ticks = pygame.time.get_ticks()

        if not self.dying:
            animation_playing = False
            if self.player_input.up:
                self.centery -= self.speed
                self.face_dir = 0
                animation_playing = True

            elif self.player_input.down:
                self.centery += self.speed
                self.face_dir = 1
                animation_playing = True

            elif self.player_input.left:
                self.centerx -= self.speed
                self.face_dir = 2
                animation_playing = True

            elif self.player_input.right:
                self.centerx += self.speed
                self.face_dir = 3
                animation_playing = True
            if animation_playing:
                self.frame_timer -= self.delta_time

            self.previous_position = self.rect.center
            self.rect.center = (self.centerx, self.centery)
            self.check_for_wall_collisions()

            if self.frame_timer <= 0:
                self.frame_timer += self.settings.pacman_animation_frame_length
                self.frame_counter += 1
                if self.frame_counter > len(self.image_frames) - 1:
                    self.frame_counter = 0
                self.current_image = self.image_frames[self.frame_counter]

            self.check_for_pellet_collisions()
            self.check_for_power_pellet_collisions()
            self.check_for_fruit_collisions()
            self.check_for_ghost_collisions()
            self.check_for_portal_collisions()

            if self.portal_cooldown_timer > 0:
                self.portal_cooldown_timer -= self.delta_time

            if self.game_master.player_input.space and self.portal_cooldown_timer <= 0:
                self.place_portal()

        else:
            self.frame_timer -= self.delta_time
            if self.frame_timer <= 0 and self.frame_counter < len(self.death_frames) - 1:
                self.frame_timer += self.settings.pacman_animation_frame_length * 6
                self.frame_counter += 1
                if self.frame_counter > len(self.death_frames) - 1:
                    self.frame_counter = 0
                self.current_image = self.death_frames[self.frame_counter]
            if self.frame_timer <= -1000:
                self.dying = False
                self.extra_lives -= 1
                if self.extra_lives < 0:
                    self.end_game_function()
                self.rect.centerx = self.spawn_position_x
                self.rect.centery = self.spawn_position_y
                self.centerx = self.spawn_position_x
                self.centery = self.spawn_position_y
                self.frame_timer = self.settings.pacman_animation_frame_length
                self.current_image = self.image_frames[0]

        self.blitme()

    def blitme(self):
        if self.face_dir == 0:
            self.screen.blit(pygame.transform.rotate(self.current_image, 270), self.rect)
        elif self.face_dir == 1:
            self.screen.blit(pygame.transform.rotate(self.current_image, 90), self.rect)
        elif self.face_dir == 2:
            self.screen.blit(self.current_image, self.rect)
        elif self.face_dir == 3:
            self.screen.blit(pygame.transform.rotate(self.current_image, 180), self.rect)

        if self.entrance_portal_rect is not None:
            self.screen.blit(self.entrance_portal_image, self.entrance_portal_rect)
        if self.exit_portal_rect is not None:
            self.screen.blit(self.exit_portal_image, self.exit_portal_rect)

    def place_portal(self):
        self.portal_cooldown_timer = 2000
        if self.entrance_portal_rect is None:
            self.entrance_portal_rect = self.entrance_portal_image.get_rect()
            self.entrance_portal_rect.center = self.rect.center
            self.fire_entrance_portal_sound.play()
        elif self.exit_portal_rect is None:
            self.exit_portal_rect = self.exit_portal_image.get_rect()
            self.exit_portal_rect.center = self.rect.center
            self.fire_exit_portal_sound.play()

    def check_for_wall_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.game_master.maze.wall_blocks, False)
        if collisions:
            self.rect.center = self.previous_position
            self.centerx = self.rect.centerx
            self.centery = self.rect.centery

    def check_for_pellet_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.game_master.maze.pellets, True)
        if collisions:
            self.game_master.scoreboard.score += 10
            self.game_master.scoreboard.update_score_text()
            if self.current_chomp_pellet_sound == 1:
                self.chomp_pellet_sound_1.play()
                self.current_chomp_pellet_sound = 2
            else:
                self.chomp_pellet_sound_2.play()
                self.current_chomp_pellet_sound = 1
            self.game_master.check_if_level_finished()

    def check_for_power_pellet_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.game_master.maze.power_pellets, True)
        if collisions:
            self.game_master.scoreboard.score += 50
            self.game_master.scoreboard.update_score_text()
            if self.current_chomp_pellet_sound == 1:
                self.chomp_pellet_sound_1.play()
                self.current_chomp_pellet_sound = 2
            else:
                self.chomp_pellet_sound_2.play()
                self.current_chomp_pellet_sound = 1
            self.game_master.check_if_level_finished()
            for ghost in self.game_master.maze.ghosts:
                ghost.induce_fear()

    def check_for_fruit_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.game_master.maze.fruit_spawner.fruits, True)
        if collisions:
            self.game_master.scoreboard.score += 200
            self.game_master.scoreboard.update_score_text()
            self.chomp_fruit_sound.play()

    def check_for_ghost_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.game_master.maze.ghosts, False)
        if collisions and not self.dying:
            self.dying = True
            self.frame_counter = 0
            self.current_image = self.death_frames[0]
            pygame.time.wait(1500)
            self.death_sound.play()
            self.last_frame_ticks = pygame.time.get_ticks()

    def check_for_portal_collisions(self):
        if self.entrance_portal_rect is not None:
            if self.rect.colliderect(self.entrance_portal_rect):
                if self.exit_portal_rect is not None and self.portal_cooldown_timer <= 0:
                    self.travel_through_portal_sound.play()
                    self.centerx = self.exit_portal_rect.centerx
                    self.centery = self.exit_portal_rect.centery
                    self.entrance_portal_rect = None
                    self.exit_portal_rect = None
        if self.exit_portal_rect is not None:
            if self.rect.colliderect(self.exit_portal_rect):
                if self.entrance_portal_rect is not None and self.portal_cooldown_timer <= 0:
                    self.travel_through_portal_sound.play()
                    self.centerx = self.entrance_portal_rect.centerx
                    self.centery = self.entrance_portal_rect.centery
                    self.entrance_portal_rect = None
                    self.exit_portal_rect = None

    def end_game_function(self):
        f = open("Highscores.txt", "r")
        highscore = f.read()
        if highscore == '':
            highscore = 0
        else:
            highscore = int(highscore)
        f.close()

        if self.game_master.scoreboard.score > highscore:
            f = open("Highscores.txt", "w+")
            f.write(str(self.game_master.scoreboard.score))
            f.close()
        self.end_game = True
