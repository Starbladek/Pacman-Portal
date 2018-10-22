import pygame
from player_input import PlayerInput
from settings import Settings
from intro_game_master import IntroGameMaster
from game_master import GameMaster


def run_game():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.display.set_caption("Pacman Portal")

    player_input = PlayerInput()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    scene = 0   # Intro

    intro_game_master = IntroGameMaster(player_input, settings, screen)
    game_master = None

    while True:
        player_input.check_events()

        if scene == 0:
            intro_game_master.update()
            if player_input.enter:
                scene = 1
                game_master = GameMaster(player_input, settings, screen)
                del intro_game_master
        elif scene == 1:
            game_master.update()
            if game_master.maze.pacman.end_game:
                scene = 0
                intro_game_master = IntroGameMaster(player_input, settings, screen)
                del game_master

        pygame.display.flip()


run_game()
