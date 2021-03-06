import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class manages bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at 0,0 and modify position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = ai_game.ship.rect.midtop

        # Store bullet position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet on the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
