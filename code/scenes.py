import pygame
from globals import COLORS, FIGURES_COLORS
from boards import Board, FakeBoard
from figures import Figures, Figure
import animations


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
        self.sprites = pygame.sprite.Group()
        self.score = 0
        self.death = False
        self.board = Board(8, 8)
        self.fake_board = FakeBoard(8, 8)
        self.figures = Figures()
        self.animation = animations.Start(self.board)

    def render(self):
        self.board.render(self.screen)
        self.fake_board.render(self.screen)
        self.figures.render(self.screen)
        if self.animation:
            self.animation = self.animation.render(self.screen)
            if self.death and not self.animation:
                pygame.quit()
        if self.death and not self.animation:
            self.animation = animations.Start(self.board)

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.figures.get_click(event.pos)

        elif event.type == pygame.MOUSEMOTION:
            self.figures.motion(event.pos)
            self.fake_board.clear()

            figure = self.figures.get_selectabled()

            if not figure:
                return

            cell = self.board.get_click((figure.rect.x, figure.rect.y))

            if cell:
                for row in range(figure.h):
                    for col in range(figure.w):
                        board_cell = self.board.get_cell((cell[0] + col, cell[1] + row))
                        if figure.figure[row][col] == 1 and (
                            board_cell is None or board_cell
                        ):
                            return
                for row in range(figure.h):
                    for col in range(figure.w):
                        if figure.figure[row][col] == 1:
                            self.fake_board.set_cell(
                                (cell[0] + col, cell[1] + row),
                                COLORS.index(figure.color),
                            )

        elif event.type == pygame.MOUSEBUTTONUP:
            figure = self.figures.get_selectabled()
            if not figure:
                return
            cell = self.board.get_click((figure.rect.x, figure.rect.y))
            if cell:
                self.set_figure(cell, figure)
                self.death = self.check_death()
            else:
                self.figures.return_to_start_pos()

    def check_death(self):
        for figure in list(self.figures.sprites):
            if self.board.check_board_set_figure(figure.figure) is True:
                return False
        return True

    def set_figure(self, cell, figure):
        for row in range(figure.h):
            for col in range(figure.w):
                board_cell = self.board.get_cell((cell[0] + col, cell[1] + row))
                if figure.figure[row][col] == 1 and (board_cell is None or board_cell):
                    self.figures.return_to_start_pos()
                    return
        for row in range(figure.h):
            for col in range(figure.w):
                if figure.figure[row][col] == 1:
                    self.board.set_cell(
                        (cell[0] + col, cell[1] + row),
                        COLORS.index(figure.color),
                    )
                    self.board.check_row_col((cell[0] + col, cell[1] + row))
        figure.remove(self.figures.sprites)
        self.fake_board.clear()
        if len(list(self.figures.sprites)) == 0:
            self.figures = Figures()
