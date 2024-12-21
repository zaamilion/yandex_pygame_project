import pygame
from globals import COLORS


class Board:
    # создание поля
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.board = [[0] * width for _ in range(height)]
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
                    pygame.Color("Grey"),
                    (
                        self.left + row * self.cell_size,
                        self.top + col * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                    1,
                )


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
                color[-1] = 100
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
