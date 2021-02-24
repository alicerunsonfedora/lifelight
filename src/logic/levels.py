#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
from typing import List, Tuple, Dict


class Level():
    def __init__(self, filepath):
        self.src = filepath
        self.tileset_name: str = ""
        self.dimensions: Tuple[int, int] = (0, 0)
        self.tile_definitions: Dict[str, Tuple[int, int]] = {" ": (-1, -1)}
        self.tiles: List[List[Tuple[int, int]]] = []

        with open(filepath, "r") as file:
            self._parse_file([lin.strip("\n") for lin in file.readlines(
            ) if lin != "\n" and not lin.startswith("#")])

    def __str__(self):
        return f"Level(tileset={self.tileset_name}, size={self.dimensions}, definitions={self.tile_definitions})"

    def _parse_file(self, source):
        if source[0] != "LIFELIGHT LEVEL":
            raise TypeError("File header for level file is corrupt.")
        source.pop(0)

        tileset_name = source.pop(0).split(" ")
        if tileset_name[0] != "TILESET":
            raise TypeError("Tileset data is missing or corrupt.")
        self.tileset_name = tileset_name[1].lower().strip()

        dimensions = source.pop(0).split("\t")
        if dimensions[0] != "SIZE":
            raise TypeError("Level dimensions is missing or corrupt.")
        self.dimensions = tuple([int(dim) for dim in dimensions[1:]])

        if source.pop(0) != "BEGIN DEFINITIONS":
            raise TypeError("Definition block is missing or corrupt.")

        while (data := source.pop(0)) != "END DEFINITIONS":
            properties = data.split("\t")
            self.tile_definitions[properties[0]] = tuple(
                [int(val) for val in properties[1:]])

        if source.pop(0) != "BEGIN LAYOUT":
            raise TypeError("Layout block is missing or corrupt.")

        while (data := source.pop(0)) != "END LAYOUT":
            self.tiles.append([self.tile_definitions[tile] for tile in data])
