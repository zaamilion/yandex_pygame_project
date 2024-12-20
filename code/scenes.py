import pygame


class Scene:
    def __init__(self, screen):
        self.screen = screen

    def render(self):
        pass

    def event(self, event):
        pass


class PlayScene(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.board = Board(10, 10)
        self.figures = []

    def render(self):
        self.board.render(self.screen)

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.board.get_click(event.pos)
            for figure in self.figures:
                if figure:
                    figure.get_click(event.pos)
        if event.type == pygame.MOUSEMOTION:
            for figure in self.figures:
                if figure:
                    figure.motion(event.pos)


class Figure:
    def __init__(self, figure: str, color: tuple, pos: tuple):
        self.figure = figure
        self.color = color
        self.x, self.y = pos
        self.size = 20
        self.selecting = False

    def render(self):
        pass

    def motion(self, pos):
        if self.selecting:
            self.x, self.y = pos

    def get_click(self, pos: tuple):
        x, y = pos
        if (
            not (self.selecting)
            and self.x <= x <= self.x + self.size
            and self.y <= y <= self.y + self.size
        ):
            self.selecting = True
            self.size = 40


class Board:
    # создание поля
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 200
        self.top = 20
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos: tuple):
        x, y = mouse_pos
        h = (x - self.left) // self.cell_size
        w = (y - self.top) // self.cell_size
        if 0 <= w < self.width and 0 <= h < self.height:
            return h, w
        return

    def on_click(self, cell_pos: tuple):
        if cell_pos:
            x, y = cell_pos
            self.board[x][y] = 1 - self.board[x][y]

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                color = pygame.Color("Black" if self.board[row][col] == 1 else "White")
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
