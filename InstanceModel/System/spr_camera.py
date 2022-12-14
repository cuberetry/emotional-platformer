from InstanceModel.spr_player import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr
from abc import ABC, abstractmethod

vec = pygame.math.Vector2


class Camera(pygame.sprite.Sprite):
    def __init__(self, player, boundary):
        super().__init__()
        gb_spr.all_sprites.add(self)
        gb_spr.camera_sprites.add(self)

        # Rendering setup
        self.player = player
        self.DISPLAY_W, self.DISPLAY_H = gb_setting.WIDTH, gb_setting.HEIGHT
        self.offset = vec(0, 0)
        self.offset_float = vec(0, 0)
        self.CONST = vec(-self.DISPLAY_W/3 + player.rect.w/3, - self.DISPLAY_H + 100)
        self.method = None
        self.right_border = boundary.right_border_x+30
        self.left_border = boundary.left_border_x

    def set_method(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()


class CamScroll(ABC):
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def scroll(self):
        pass


class Follow(CamScroll):
    def __init(self, camera, player):
        CamScroll.__init__(self, camera, player)

    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)


class Border(CamScroll):
    def __init(self, camera, player):
        CamScroll.__init__(self, camera, player)

    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
        self.camera.offset.x = max(self.camera.left_border, self.camera.offset.x)
        self.camera.offset.x = min(self.camera.offset.x, self.camera.right_border - self.camera.DISPLAY_W)


class Auto(CamScroll):
    def __init(self, camera, player):
        CamScroll.__init__(self, camera, player)

    def scroll(self):
        self.camera.offset.x += 1
