import pygame
import sys

class Stars:
    """Overall class to manage the asset(s) and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        