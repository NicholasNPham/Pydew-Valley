import pygame
from settings import *


class Transition:
    def __init__(self, reset, player):

        # Setup
        self.display_surface = pygame.display.get_surface()
        self.reset = reset
        self.player = player

        # Overlay Image
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.color = 225
        self.speed = -2

    def play(self):

        self.color += self.speed
        if self.color <= 0:
            self.speed *= -1
            self.color = 0
            # 1. Call Reset
            self.reset()
        if self.color > 255:
            self.color = 255
            # 2. Wake Player Up
            self.player.sleep = False
            # 3. Set the speed to -2 at the end of the transition
            self.speed = -2

        self.image.fill((self.color, self.color, self.color))
        self.display_surface.blit(self.image, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
