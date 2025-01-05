import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Class to represent a single star in the sky."""

    def __init__(self, star_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = star_game.screen

        # Load the star image and set itss rect attribute.
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)