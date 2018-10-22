from pacman import Pacman
from maze import Maze
from scoreboard import Scoreboard


class GameMaster:
    def __init__(self, player_input, settings, screen):
        self.settings = settings
        self.screen = screen
        self.player_input = player_input

        self.pacman = Pacman(self)
        self.maze = Maze(self)
        self.scoreboard = Scoreboard(self)

    def update(self):
        self.screen.fill(self.settings.bg_color)
        self.pacman.update()
        self.maze.draw_all_maze_things()
        self.scoreboard.show_score()

    def check_if_level_finished(self):
        if len(self.maze.pellets) == 0 and len(self.maze.power_pellets) == 0:
            self.scoreboard.level += 1
            self.scoreboard.update_level_text()
            del self.maze
            self.maze = Maze(self)
