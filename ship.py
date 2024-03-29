import pygame


class Ship(pygame.sprite.Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        """Init ship and set starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship starts at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Save ship coords in float
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        self.center = self.screen_rect.centerx


    def update(self):
        """Refresh ship pos according to flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draws a ship at current pos"""
        self.screen.blit(self.image, self.rect)
