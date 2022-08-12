from turtle import Screen
import pygame
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship

class Bullet(Sprite):
    def __init__(self, ai_settings: Settings, screen, ship: Ship) -> None:
        super().__init__()
        self.screen = screen

        # Create a bullet, put it to ship position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # update bullet position
        self.y -= self.speed_factor
        # update bullet's object pos
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)