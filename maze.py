from pygame.sprite import Group
from wall_block import WallBlock
from pellet import Pellet
from power_pellet import PowerPellet
from fruit_spawner import FruitSpawner
from ghost_blinky import GhostBlinky
from ghost_pinky import GhostPinky
from ghost_inky import GhostInky
from ghost_clyde import GhostClyde


class Maze:

    def __init__(self, game_master):
        self.game_master = game_master
        self.screen = game_master.screen
        self.screen_rect = game_master.screen.get_rect()

        self.pacman = game_master.pacman
        self.fruit_spawner = None

        self.wall_blocks = Group()
        self.pellets = Group()
        self.power_pellets = Group()

        self.ghosts = Group()
        self.ghost_blinky = GhostBlinky(game_master)
        self.ghost_pinky = GhostPinky(game_master)
        self.ghost_inky = GhostInky(game_master)
        self.ghost_clyde = GhostClyde(game_master)
        self.ghosts.add(self.ghost_blinky)
        self.ghosts.add(self.ghost_pinky)
        self.ghosts.add(self.ghost_inky)
        self.ghosts.add(self.ghost_clyde)

        self.create_maze()

    def create_maze(self):
        f = open("Maze Text.txt", "r")

        if f.mode == 'r':
            content = f.readlines()
            row_counter = 0

            for line in content:
                column_counter = 0
                for index in line:
                    if index == 'X':
                        wb = WallBlock(self.game_master)
                        wb.rect.center = (
                            (column_counter * wb.rect.width) + 40,
                            (row_counter * wb.rect.height) + 60
                        )
                        self.wall_blocks.add(wb)
                    elif index == 'P':
                        self.pacman.rect.center = (
                            (column_counter * self.game_master.settings.wall_block_scale) + 40,
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                        )
                        self.pacman.centerx = self.pacman.rect.centerx
                        self.pacman.centery = self.pacman.rect.centery
                        self.pacman.spawn_position_x = self.pacman.centerx
                        self.pacman.spawn_position_y = self.pacman.centery
                    elif index == 'F':
                        self.fruit_spawner = FruitSpawner(self.game_master)
                        self.fruit_spawner.fruit_spawn_position_x =\
                            (column_counter * self.game_master.settings.wall_block_scale) + 40
                        self.fruit_spawner.fruit_spawn_position_y =\
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                    elif index == 'o':
                        pellet = Pellet(self.screen)
                        pellet.rect.center = (
                            (column_counter * self.game_master.settings.wall_block_scale) + 40,
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                        )
                        self.pellets.add(pellet)
                    elif index == 'O':
                        power_pellet = PowerPellet(self.screen)
                        power_pellet.rect.center = (
                            (column_counter * self.game_master.settings.wall_block_scale) + 40,
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                        )
                        self.power_pellets.add(power_pellet)
                    elif index == '1':
                        self.ghost_blinky.rect.center = (
                            (column_counter * self.game_master.settings.wall_block_scale) + 40,
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                        )
                    elif index == '2':
                        self.ghost_pinky.rect.center = (
                            (column_counter * self.game_master.settings.wall_block_scale) + 40,
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                        )
                    elif index == '3':
                        self.ghost_inky.rect.center = (
                            (column_counter * self.game_master.settings.wall_block_scale) + 40,
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                        )
                    elif index == '4':
                        self.ghost_clyde.rect.center = (
                            (column_counter * self.game_master.settings.wall_block_scale) + 40,
                            (row_counter * self.game_master.settings.wall_block_scale) + 60
                        )
                    column_counter += 1
                row_counter += 1

    def draw_all_maze_things(self):
        for wb in self.wall_blocks:
            wb.update()
        for pellet in self.pellets:
            pellet.update()
        for power_pellet in self.power_pellets:
            power_pellet.update()
        for ghost in self.ghosts:
            ghost.update()
        self.fruit_spawner.update()
