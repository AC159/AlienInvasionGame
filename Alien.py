import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # A class that represents a single alien in the fleet

    def __init__(self, ai_settings, screen):
        # Initialize the alien and set its starting position
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute:
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen
        self.rect.left = self.rect.width
        self.rect.top = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.left)

    def blitme(self):
        # Draw the alien at its current location
        self.screen.blit(self.image, (self.rect.top, self.rect.left))

    def update(self):
        # Move alien to the right or left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.left = self.x

    def check_edges(self):
        # Return true if an alien is at edge of the screen
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
