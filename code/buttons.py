import pygame
pygame.font.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, parent, group, w, h, pos=(0,0),font=pygame.font.Font(None, 30), text='text', button_color=(0,0,0,0), text_color=(255,255,255,255), border_width=0, border_radius=-1):
        super().__init__(group)
        self.parent = parent
        self.w, self.h = w,h
        self.image = pygame.Surface((w,h), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        pygame.draw.rect(self.image, button_color, (0,0,w,h), border_width, border_radius)

        surface = font.render(text, False, text_color)
        self.image.blit(surface, (0,0))
    def get_click(self,pos):
        if self.rect.x <= pos[0] <= self.rect.x + self.w and self.rect.y <= pos[1] <= self.rect.y + self.h:
            return self.on_click()
        return None
    def on_click(self):
        pass

class PlayButton(Button):
    def on_click(self):
        self.parent.game.resume_game()