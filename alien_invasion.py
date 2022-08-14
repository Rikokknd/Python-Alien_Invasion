import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
import game_functions as gf


def run_game():
    """Init game and make a window object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    play_button = Button(ai_settings, screen, "Play")

    # Create ship
    ship = Ship(ai_settings, screen)

    # create bullet group
    bullets = Group()

    # create alien fleet
    aliens = Group()
    gf.create_alien_fleet(ai_settings, screen, ship, aliens)
    
    clock = pygame.time.Clock()
    # start the main loop for the game
    while True:
        clock.tick(180)
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

if __name__ == "__main__":
    run_game()
