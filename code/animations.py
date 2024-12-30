import pygame
from boards import Board
import random
from globals import FIGURES_COLORS
from copy import deepcopy


class Start:
    def __init__(self, board):
        self.running = True
        self.game_board = deepcopy(board.board)
        self.board = Board(board.width, board.height)
        self.board.board = deepcopy(board.board)
        self.start_time = pygame.time.get_ticks()
        self.level = 1

    def render(self, screen):
        self.board.render(screen)
        if pygame.time.get_ticks() - self.start_time > 50 * self.level:
            if self.level <= self.board.height:
                for i in range(self.board.width):
                    if self.board.board[i][-self.level] == 0:
                        self.board.board[i][-self.level] = random.randint(
                            1, len(FIGURES_COLORS)
                        )
            else:
                for j in range(self.board.width):
                    if (
                        self.board.board[j][self.level - self.board.height - 1]
                        != self.game_board[j][self.level - self.board.height - 1]
                    ):
                        self.board.board[j][self.level - self.board.height - 1] = 0
            if self.level == (self.board.height * 2):
                self.running = False
                self = None
                return
            self.level += 1
        return self
