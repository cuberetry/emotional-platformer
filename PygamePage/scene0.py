import sys
from InstanceModel.spr_tilemap import *
from InstanceModel.spr_camera import *
from InstanceModel.spr_player import *
from InstanceModel.spr_boundary import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr


class Scene:
    def __init__(self):
        self.P1 = Player()

        # Load stage
        self.scene_map = TileMap(gb_setting.ROOT_PATH + "/StageData/stage01.csv")
        self.P1.rect.x, self.P1.rect.y = self.scene_map.start_x, self.scene_map.start_y

        self.boundary_map = BoundaryMap(gb_setting.ROOT_PATH + "/StageData/stage01.csv")
        self.boundary = Boundary(self.P1, self.boundary_map)

        self.camera = Camera(self.P1)
        self.follow = Follow(self.camera, self.P1)
        self.border = Border(self.camera, self.P1)
        self.auto = Auto(self.camera, self.P1)
        self.camera.set_method(self.border)

    def mainloop(self):
        self.P1.move()
        self.boundary.line()
        self.P1.update()
        for entity in gb_spr.enemy_sprites:
            entity.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        gb_var.SURFACE.fill((0, 0, 0))
        if gb_var.IS_PAUSING:
            return

        self.camera.scroll()
        for entity in gb_spr.all_sprites:
            if entity in gb_spr.camera_sprites:
                continue
            gb_var.SURFACE.blit(entity.surf, (entity.rect.x - self.camera.offset.x,
                                              entity.rect.y - self.camera.offset.y))

        pygame.display.update()
        gb_var.FPS.tick(gb_setting.MAXFPS)
