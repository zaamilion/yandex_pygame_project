import pygame
import sys

FPS = 60
SIZE = WIDTH, HEIGHT = 800, 400


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("CLash of Drons")
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        self.current_scene = 0

    def event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)

    def render(self):
        self.current_scene.render()


def main():
    game = Game()
    while True:
        for event in pygame.event.get():
            game.event(event)
        game.render()
        game.clock.tick(FPS)


if __name__ == "__main__":
    main()
