import pygame, csv, os
import GlobalVariable.sprite_group as gb_spr
import GlobalVariable.game_var as gb_var

vec = pygame.math.Vector2


class Platform(pygame.sprite.Sprite):
    def __init__(self, state, x, y):
        super().__init__()
        gb_spr.all_sprites.add(self)
        gb_spr.env_sprites.add(self)

        # Rendering setup
        self.surf = pygame.Surface((16, 16))
        self.surf.fill(state)
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.surf, (self.rect.x, self.rect.y))


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
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '0':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '1':
                    tiles.append(Platform(gb_var.PLATFORM_STATE_COLOR['np'], x * self.tile_size, y * self.tile_size))
                elif tile == '2':
                    tiles.append(Platform(gb_var.PLATFORM_STATE_COLOR['hp'], x * self.tile_size, y * self.tile_size))
                elif tile == '3':
                    tiles.append(Platform(gb_var.PLATFORM_STATE_COLOR['ap'], x * self.tile_size, y * self.tile_size))
                elif tile == '4':
                    tiles.append(Platform(gb_var.PLATFORM_STATE_COLOR['sp'], x * self.tile_size, y * self.tile_size))
                elif tile == '5':
                    tiles.append(Platform(gb_var.PLATFORM_STATE_COLOR['wp'], x * self.tile_size, y * self.tile_size))

                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
