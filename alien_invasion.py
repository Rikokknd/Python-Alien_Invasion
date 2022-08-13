import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    """Init game and make a window object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create ship
    ship = Ship(ai_settings, screen)

    # create bullet group
    bullets = Group()

    # create alien fleet
    aliens = Group()
    gf.create_alien_fleet(ai_settings, screen, ship, aliens)
    

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

if __name__ == "__main__":
    run_game()
