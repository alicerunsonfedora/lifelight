#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

from os import path
from typing import Tuple
from src.logic.player import Player
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
            asset_path("assets/tilesheets/struct.png"), (48, 48), (12, 16))

        self.player = Player((200, 200), 4)

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
        self.canvas.fill(self.palette.get_color("DARK_BLACK"))
        self.canvas.blit(self.ts_structures.get_tile(
            2, 3), self.player.position)

    def render(self) -> None:
        """Render the changes onto the screen."""
        pygame.display.update()
