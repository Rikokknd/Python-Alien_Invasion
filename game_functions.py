import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets: pygame.sprite.Group):
    # Track mouse and keyboard events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)

def check_keydown_events(event, ai_settings, screen, ship, bullets: pygame.sprite.Group):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ai_settings, screen, ship, bullets: pygame.sprite.Group):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets: pygame.sprite.Group):
    # apply background color.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # display last drawn screen.
    pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def update_bullets(bullets):
    bullets.update()
    # removing out of bounds bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_alien_fleet(ai_settings, screen, ship, aliens):

    def get_number_aliens_in_row(ai_settings, alien_width):
        available_space_width = ai_settings.screen_width - 2 * alien_width
        number_of_aliens_in_row = int(available_space_width / (2 * alien_width))
        return number_of_aliens_in_row

    def get_number_rows(ai_settings, ship_height, alien_height):
        available_space_for_rows = (ai_settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_for_rows / (2 * alien_height))
        return number_rows

    def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)

    alien = Alien(ai_settings, screen)
    number_of_aliens_in_row = get_number_aliens_in_row(ai_settings, alien.rect.width)
    number_of_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # creating rows
    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens_in_row):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)