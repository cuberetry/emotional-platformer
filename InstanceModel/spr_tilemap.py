import pygame
import csv
import os
import GlobalVariable.game_var as gb_var
import InstanceModel.spr_platform as platform


class TileMap:
    def __init__(self, filename):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0

        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):
        mapp = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                mapp.append(list(row))
        return mapp

    def load_tiles(self, filename):
        tiles = []
        mapp = self.read_csv(filename)
        x, y = 0, 0
        for row in mapp:
            x = 0
            for tile in row:
                if tile == '0':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '1':
                    tiles.append(platform.Platform(gb_var.PLATFORM_STATE_COLOR['np'], x * self.tile_size, y * self.tile_size))
                elif tile == '2':
                    tiles.append(platform.Platform(gb_var.PLATFORM_STATE_COLOR['hp'], x * self.tile_size, y * self.tile_size))
                elif tile == '3':
                    tiles.append(platform.Platform(gb_var.PLATFORM_STATE_COLOR['ap'], x * self.tile_size, y * self.tile_size))
                elif tile == '4':
                    tiles.append(platform.Platform(gb_var.PLATFORM_STATE_COLOR['sp'], x * self.tile_size, y * self.tile_size))
                elif tile == '5':
                    tiles.append(platform.Platform(gb_var.PLATFORM_STATE_COLOR['wp'], x * self.tile_size, y * self.tile_size))

                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile mapp
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
