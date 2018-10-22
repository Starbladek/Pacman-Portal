import sys
import pygame


class PlayerInput:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.enter = False
        self.space = False

    def check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

                if event.key == pygame.K_UP:
                    self.up = True
                elif event.key == pygame.K_DOWN:
                    self.down = True
                elif event.key == pygame.K_LEFT:
                    self.left = True
                elif event.key == pygame.K_RIGHT:
                    self.right = True
                elif event.key == pygame.K_RETURN:
                    self.enter = True
                elif event.key == pygame.K_SPACE:
                    self.space = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up = False
                elif event.key == pygame.K_DOWN:
                    self.down = False
                elif event.key == pygame.K_LEFT:
                    self.left = False
                elif event.key == pygame.K_RIGHT:
                    self.right = False
                elif event.key == pygame.K_RETURN:
                    self.enter = False
                elif event.key == pygame.K_SPACE:
                    self.space = False
