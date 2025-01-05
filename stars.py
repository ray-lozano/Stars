import pygame
from settings import Settings
from star import Star
import sys

class Stars:
    """Overall class to manage the asset(s) and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()    # Initalized clock to run at a set fps.
        self.settings = Settings()

        # Set the screen window.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        # Star setup
        #self.star = Star(self)
        self.stars = pygame.sprite.Group()

        self._create_stars()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)     # Have the game run at 60 fps.

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            # If the player closes the window, then exit.
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_stars(self):
        """Create the rows of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size        # Get the star width and height.
        
        # Set the current x and y to the star's width and height
        current_x, current_y = star_width, star_height

        # Loop to create the rows of stars.
        # Setting the width and height between stars to be the width and height of a star.
        # The current x and y values will be the positions of where the next star will go.
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                # Create a star at the current x and y position
                self._create_star(current_x, current_y)
                current_x += 2 * star_width     # Leaves space between the previous and current x value exactly one star size.
            
            # Once a row is finished, reset the x value to the beginning of the row,
            # and increment the y value to start the new row.
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """Creates a star."""
        # x_position is the location in the row that the star is placed.
        # y_position is the current row for the stars.
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()            


if __name__ == '__main__':
    # Make the game instance and run the game.
    s = Stars()
    s.run_game()