from globals import COLORS, FIGURES_COLORS
import pygame
import random


class Figures:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        x, y = 500, 100
        for _ in range(3):
            figure = Figure(random.choice(FIGURES), self.sprites)
            figure.set_color(random.choice(FIGURES_COLORS))
            figure.set_pos((x, y))
            y += 150

    def render(self, screen):
        self.sprites.draw(screen)

    def get_click(self, pos):
        for figure in list(self.sprites):
            if figure:
                figure.get_click(pos)

    def motion(self, pos):
        for figure in list(self.sprites):
            if figure:
                figure.motion(pos)

    def return_to_start_pos(self):
        for figure in list(self.sprites):
            if figure:
                figure.return_to_start_pos()

    def get_selectabled(self):
        for figure in list(self.sprites):
            if figure:
                if figure.selecting_pos:
                    return figure


class Figure(pygame.sprite.Sprite):
    def __init__(
        self,
        figure: list,
        group: pygame.sprite.Group,
        color: pygame.Color = pygame.Color("Black"),
        pos: tuple = (0, 0),
    ):
        super().__init__(group)
        self.figure = figure
        self.h = len(self.figure)
        self.w = len(self.figure[0])
        self.block_size = 35
        self.counter = sum([sum(i) for i in self.figure])
        self.image = pygame.Surface(
            (self.w * self.block_size, self.h * self.block_size), pygame.SRCALPHA, 32
        )
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.color = color
        self.stroke_color = tuple(
            [i - 100 if i >= 100 else i for i in list(self.color)[:-1]]
        )
        self.start_pos = pos
        self.selecting_pos = None

        self.update_img()

    def update_img(self):
        self.image = pygame.Surface(
            (self.w * self.block_size, self.h * self.block_size), pygame.SRCALPHA, 32
        )
        for y in range(self.h):
            for x in range(self.w):
                if self.figure[y][x] == 1:
                    pygame.draw.rect(
                        self.image,
                        self.color,
                        (
                            x * self.block_size,
                            y * self.block_size,
                            self.block_size,
                            self.block_size,
                        ),
                    )
                    pygame.draw.rect(
                        self.image,
                        self.stroke_color,
                        (
                            x * self.block_size,
                            y * self.block_size,
                            self.block_size,
                            self.block_size,
                        ),
                        1,
                    )

    def set_color(self, color: pygame.Color):
        self.color = color
        self.stroke_color = tuple(
            [i - 100 if i >= 100 else i for i in list(self.color)[:-1]]
        )
        self.update_img()

    def set_pos(self, pos: tuple):
        self.rect.x, self.rect.y = pos
        self.start_pos = pos

    def motion(self, pos):
        if self.selecting_pos:
            self.rect.x, self.rect.y = (
                pos[0] + self.selecting_pos[0],
                pos[1] + self.selecting_pos[1],
            )

    def return_to_start_pos(self):
        if self.selecting_pos:
            self.selecting_pos = None
            self.rect.x, self.rect.y = self.start_pos
            self.block_size = 30

    def get_click(self, pos: tuple):
        x, y = pos
        if (
            not (self.selecting_pos)
            and self.rect.x - 10 <= x <= self.rect.x + self.block_size * self.w + 10
            and self.rect.y - 10 <= y <= self.rect.y + self.block_size * self.h + 10
        ):
            self.selecting_pos = (self.rect.x - x, self.rect.y - y)
            self.block_size = 40
            self.update_img()


FIGURES = [
    [[1, 1]],  # 2x1 block
    [[1, 1, 1]],  # 3x1 block
    [[1, 1, 1, 1]],  # 4x1 block
    [[1, 1, 1, 1, 1]],  # 5x1 block
    [[1, 1], [1, 1]],  # 2x2 block
    [[1, 1, 1, 1], [1, 1, 1, 1]],  # 4x2 block
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # 3x3 block
    [[1, 1, 1], [1, 0, 0], [1, 0, 0]],  # 3x3 - 2x2 block
    [[1, 1], [1, 0]],  # 2x2 - 2x1 block
    [[1, 1, 1], [1, 0, 0]],  # Tetris L block
    [[1, 1, 1], [0, 0, 1]],  # Tetris J block
    [[1, 1, 1], [0, 1, 0]],  # Tetris T block
    [[1, 1], [0, 1], [0, 1]],  # Tetris S block
    [[1, 1], [1, 0], [1, 0]],  # Tetris Z block
    [[1, 0], [0, 1]],  # Diagonal 2x2 block
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],  # Diagonal 3x3 block
]
