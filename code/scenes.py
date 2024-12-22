import pygame
from globals import COLORS, FIGURES_COLORS
from boards import Board, FakeBoard
from figures import Figures, Figure


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
        self.score = 0
        self.board = Board(10, 10)
        self.fake_board = FakeBoard(10, 10)
        self.figures = Figures()

    def render(self):
        self.board.render(self.screen)
        self.fake_board.render(self.screen)
        self.figures.render(self.screen)

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.figures.get_click(event.pos)

        if event.type == pygame.MOUSEMOTION:
            self.figures.motion(event.pos)
            self.fake_board.clear()

            figure = self.figures.get_selectabled()

            if not figure:
                return

            cell = self.board.get_click((figure.x, figure.y))

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

        if event.type == pygame.MOUSEBUTTONUP:
            figure = self.figures.get_selectabled()
            if not figure:
                return
            cell = self.board.get_click((figure.x, figure.y))
            if cell:
                for row in range(figure.h):
                    for col in range(figure.w):
                        board_cell = self.board.get_cell((cell[0] + col, cell[1] + row))
                        if figure.figure[row][col] == 1 and (
                            board_cell is None or board_cell
                        ):
                            self.figures.return_to_start_pos()
                            return
                for row in range(figure.h):
                    for col in range(figure.w):
                        if figure.figure[row][col] == 1:
                            self.board.set_cell(
                                (cell[0] + col, cell[1] + row),
                                COLORS.index(figure.color),
                            )
                            print(self.board.check_row_col(cell))
                self.figures.figures.remove(figure)
                self.fake_board.clear()
                if not self.figures.figures:
                    self.figures = Figures()

            else:
                self.figures.return_to_start_pos()
