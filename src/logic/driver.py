#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

from os import path
import pygame
from src.assets import Tilesheet, ColorPalette


class Lifelight():
    """The main application class for the game."""

    def __init__(self):
        """Set up the game's canvas, colors, tilesheets, and event listeners."""

        self.canvas = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Lifelight")

        self.frame_limiter = pygame.time.Clock()
        self.frame_limiter.tick(60)

        self.palette = ColorPalette(path.join("assets", "adventure28.gpl"))
        self.palette.assign_color_name("DARK_BLACK", "091d21")

        self.ts_structures = Tilesheet(
            path.join("assets", "tilesheets", "struct.png"), (48, 48), (12, 16))

    def manage_game_events(self):
        """Loop through the game events and return if the game should quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update_canvas(self):
        """Update the contents of the canvas."""
        self.canvas.fill(self.palette.get_color("DARK_BLACK"))
        self.canvas.blit(self.ts_structures.get_tile(2, 3), (200, 200))

    def render(self):
        """Render the changes onto the screen."""
        pygame.display.update()
