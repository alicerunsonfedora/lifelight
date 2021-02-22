#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

from os import path
import pygame
from pygame import locals
from src.assets import Tilesheet, ColorPalette

pygame.init()

WINDOW = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Lifelight")

FRAME_LIMIT = pygame.time.Clock()
FRAME_LIMIT.tick(60)


def main():
    """Execute the main game loop."""

    # Start the game.
    in_game = True

    struct_ts = Tilesheet(path.join("assets", "tilesheets",
                                    "struct.png"), (48, 48), (12, 16))

    a28 = ColorPalette(path.join("assets", "adventure28.gpl"))
    a28.assign_color_name("DARK_BLACK", "091d21")

    WINDOW.fill(a28.get_color("DARK_BLACK"))

    # While we're in game, keep running this loop.
    while in_game:

        # Iterate through the various events that PyGame is listening to.
        for event in pygame.event.get():

            # Cause a break in the loop if we've received the quit event.
            if event.type == pygame.QUIT:
                in_game = False

        WINDOW.blit(struct_ts.get_tile(2, 3), (200, 200))

        # Update the display buffer.
        pygame.display.update()

    # Close out of the game when we exit the loop.
    pygame.quit()


if __name__ == "__main__":
    main()
