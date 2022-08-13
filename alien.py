import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen) -> None:
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load image, define rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # position in top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        # draw alien
        self.screen.blit(self.image, self.rect)