import pygame
from globals import COLORS
import random
from copy import deepcopy
class Board:
    # создание поля
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.board = deepcopy(random.choice(BOARDS))
        # self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 20
        self.top = 100
        self.cell_size = 40

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos: tuple):
        x, y = mouse_pos
        h = (x - self.left) // self.cell_size
        w = (y - self.top) // self.cell_size
        if 0 <= w < self.width and 0 <= h < self.height:
            return h, w
        return

    def get_cell(self, cell):
        if 0 <= cell[1] < self.width and 0 <= cell[0] < self.height:
            return self.board[cell[0]][cell[1]]
        return

    def set_cell(self, cell: tuple, value: int):
        if 0 <= cell[0] < self.height and 0 <= cell[1] < self.width:
            self.board[cell[0]][cell[1]] = value

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                color = COLORS[self.board[row][col]]
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        self.left + row * self.cell_size,
                        self.top + col * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )
                pygame.draw.rect(
                    screen,
                    (0, 0, 20),
                    (
                        self.left + row * self.cell_size,
                        self.top + col * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                    1,
                )

    def break_row_col(self, cell: tuple):
        res = 0
        if self.check_row(cell):
            self.break_row(cell[0])
            res += 1

        if self.check_col(cell):
            self.break_col(cell[1])
            res += 1
        
        return res

    def check_row(self, cell: tuple) -> int:
        for x in range(0, self.width):
            if self.board[cell[0]][x] == 0 and x != cell[1]:
                return 0
        return 1

    def check_col(self, cell: tuple) -> int:
        for y in range(0, self.height):
            if self.board[y][cell[1]] == 0 and y != cell[0]:
                return 0
        return 1

    def check_board_set_figure(self, figure: list) -> bool:
        for row in range(self.height):
            for col in range(self.width):
                res = self.check_cell_set_figure(
                    (
                        row,
                        col,
                    ),
                    figure,
                )
                if res is True:
                    return True
        return False

    def check_cell_set_figure(self, cell: tuple, figure: list) -> bool:
        for y in range(len(figure)):
            for x in range(len(figure[0])):
                if 0 <= cell[0] + y < self.height and 0 <= cell[1] + x < self.width:
                    if figure[y][x] == 1 and self.board[cell[0] + y][cell[1] + x] != 0:
                        return False
                else:
                    return False
        return True

    def break_row(self, row):
        for x in range(0, self.width):
            self.board[row][x] = 0

    def break_col(self, col):
        for y in range(0, self.height):
            self.board[y][col] = 0


class FakeBoard(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def clear(self):
        self.board = [[0] * self.width for _ in range(self.height)]

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                color = COLORS[self.board[row][col]]
                color = list(color)
                color = tuple([i + 50 if i <= 200 else i - 20 for i in color])
                stroke_color = (50,50,50)
                if self.board[row][col] != 0:
                    pygame.draw.rect(
                        screen,
                        color,
                        (
                            self.left + row * self.cell_size,
                            self.top + col * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                    )
                    pygame.draw.rect(
                        screen,
                        stroke_color,
                        (
                            self.left + row * self.cell_size,
                            self.top + col * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                        1
                    )


BOARDS = [
    # empty
    [[0] * 8 for _ in range(8)], 
          # Z
          [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]]]