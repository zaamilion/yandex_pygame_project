import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
    
    def render(self, screen, pos=(500,50)):
        surface = self.font.render(str(self.score), False, (255,255,255))
        screen.blit(surface, pos)
        