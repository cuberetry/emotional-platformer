import pygame
import csv
import os
import InstanceModel.spr_platform as platform
import InstanceModel.spr_neutral_platform as neu_p
import InstanceModel.spr_happy_platform as hap_p
import InstanceModel.spr_fire_platform as fire_p
import InstanceModel.spr_ice_platform as ice_p


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
                    tiles.append(platform.Platform(x * self.tile_size, y * self.tile_size))
                elif tile == '2':
                    tiles.append(neu_p.NeuPlatform(x * self.tile_size, y * self.tile_size))
                elif tile == '3':
                    tiles.append(hap_p.HapPlatform(x * self.tile_size, y * self.tile_size))
                elif tile == '4':
                    tiles.append(fire_p.FirePlatform(x * self.tile_size, y * self.tile_size))
                elif tile == '5':
                    tiles.append(ice_p.IcePlatform(x * self.tile_size, y * self.tile_size))

                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile mapp
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles



