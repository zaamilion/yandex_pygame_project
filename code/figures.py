from globals import COLORS, FIGURES_COLORS
import pygame
import random


class Figures:
    def __init__(self):
        self.figures = [random.choice(FIGURES) for _ in range(3)]
        x, y = 500, 100
        for figure in self.figures:
            figure.set_color(random.choice(FIGURES_COLORS))
            figure.set_pos((x, y))
            y += 150

    def render(self, screen):
        for figure in self.figures:
            if figure:
                figure.render(screen)

    def get_click(self, pos):
        for figure in self.figures:
            if figure:
                figure.get_click(pos)

    def motion(self, pos):
        for figure in self.figures:
            if figure:
                figure.motion(pos)

    def return_to_start_pos(self):
        for figure in self.figures:
            if figure:
                figure.return_to_start_pos()

    def get_selectabled(self):
        for figure in self.figures:
            if figure:
                if figure.selecting_pos:
                    return figure


class Figure:
    def __init__(
        self,
        figure: list,
        color: pygame.Color = pygame.Color("Black"),
        pos: tuple = (0, 0),
    ):
        self.figure = figure
        self.h = len(self.figure)
        self.w = len(self.figure[0])
        self.color = color
        self.stroke_color = tuple(
            [i - 100 if i >= 100 else i for i in list(self.color)[:-1]]
        )
        self.x, self.y = pos
        self.start_pos = pos
        self.block_size = 35
        self.selecting_pos = None

    def set_color(self, color: pygame.Color):
        self.color = color
        self.stroke_color = tuple(
            [i - 100 if i >= 100 else i for i in list(self.color)[:-1]]
        )

    def set_pos(self, pos: tuple):
        self.x, self.y = pos
        self.start_pos = pos

    def render(self, screen):
        for h in range(self.h):
            for w in range(self.w):
                if self.figure[h][w] == 1:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            self.x + w * self.block_size,
                            self.y + h * self.block_size,
                            self.block_size,
                            self.block_size,
                        ),
                    )
                    pygame.draw.rect(
                        screen,
                        self.stroke_color,
                        (
                            self.x + w * self.block_size,
                            self.y + h * self.block_size,
                            self.block_size,
                            self.block_size,
                        ),
                        1,
                    )

    def motion(self, pos):
        if self.selecting_pos:
            self.x, self.y = (
                pos[0] + self.selecting_pos[0],
                pos[1] + self.selecting_pos[1],
            )

    def return_to_start_pos(self):
        if self.selecting_pos:
            self.selecting_pos = None
            self.x, self.y = self.start_pos
            self.block_size = 30

    def get_click(self, pos: tuple):
        x, y = pos
        if (
            not (self.selecting_pos)
            and self.x - 10 <= x <= self.x + self.block_size * self.w + 10
            and self.y - 10 <= y <= self.y + self.block_size * self.h + 10
        ):
            self.selecting_pos = (self.x - x, self.y - y)
            self.block_size = 40


FIGURES = [
    Figure([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
    Figure([[0, 1], [1, 1], [1, 0]]),
    Figure([[1, 1, 1, 1]]),
    Figure([[0, 0, 1], [0, 0, 1], [1, 1, 1]]),
    Figure([[1, 1, 1], [1, 0, 0], [1, 0, 0]]),
    Figure([[1, 1], [1, 1]]),
    Figure([[1, 0, 0], [1, 1, 1]]),
    Figure([[1], [1], [1], [1]]),
    Figure([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
    Figure([[1, 0], [1, 1], [1, 0]]),
]
