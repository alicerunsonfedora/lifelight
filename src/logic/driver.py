#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

from os import path
from typing import Tuple
from src.logic.player import Player
from src.data.levels import Level
import pygame
from src.assets import Tilesheet, ColorPalette, asset_path


class Lifelight():
    """The main application class for the game."""

    def __init__(self, window_size: Tuple[int, int] = (1280, 720), fps: int = 60) -> None:
        """Set up the game's canvas, colors, tilesheets, and event listeners."""

        self.canvas = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Lifelight")

        self.frame_limiter = pygame.time.Clock()
        self.fps = fps

        self.palette = ColorPalette(asset_path("assets/adventure28.gpl"))
        self.palette.assign_color_name("DARK_BLACK", "091d21")

        self.ts_structures = Tilesheet(
            asset_path("assets/tilesheets/struct01.png"), (48, 48), (12, 16))

        self.player = Player((200, 200), 4)
        self.level = Level(asset_path("data/random01.lvl"))

    def manage_game_events(self) -> bool:
        """Manage the primary game events such as quitting, player movement, etc."""
        self.frame_limiter.tick(self.fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pressed = pygame.key.get_pressed()
        self.player.update_position(pressed)

        return True

    def update_canvas(self) -> None:
        """Update the contents of the canvas."""

        # Fill the canvas with a black-like color.
        self.canvas.fill(self.palette.get_color("DARK_BLACK"))

        # Set up the tile sequencers.
        tx, ty = 16, 16  # TODO: Get these tiles centered!
        width, height = self.ts_structures.tile_size

        # Iterate through all of the tilemap rows, filling the tilemap slowly.
        for row in self.level.tiles:

            # Fill in the tile with the appropriate tileset image at that position, or don't fill anything if the tile
            # is an "air" tile.
            for cx, cy in row:
                if cx != -1 and cy != -1:
                    self.canvas.blit(
                        self.ts_structures.get_tile(cx, cy), (tx, ty))
                tx += width

            # Move to the next row and reset the X position.
            ty += height
            tx = 16

    def render(self) -> None:
        """Render the changes onto the screen."""
        pygame.display.update()
