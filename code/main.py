import pygame
import sys
from scenes import *
import animations

FPS = 60
SIZE = WIDTH, HEIGHT = 800, 600


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Block Blast")
        self.screen = pygame.display.set_mode(SIZE)
        self.surf = pygame.Surface(SIZE, pygame.SRCALPHA, 32)
        self.clock = pygame.time.Clock()
        self.game_scene = PlayScene(self, self.surf)
        self.menu_scene = MenuScene(self, self.surf)
        self.current_scene = self.menu_scene
    def event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            self.current_scene.event(event)

    def render(self):
        self.surf.fill((159, 79, 255))
        self.current_scene.render()
        self.screen.blit(self.surf, (0, 0))
        pygame.display.flip()
    
    def resume_game(self):
        self.current_scene = self.game_scene
        self.game_scene.animation = animations.Start(self.game_scene.board)
    
    def end_game(self):
        self.go_menu()
        self.game_scene = PlayScene(self, self.surf)
    
    def go_menu(self):
        self.current_scene = self.menu_scene


def main():
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            game.event(event)
        game.render()
        game.clock.tick(FPS)


if __name__ == "__main__":
    main()
