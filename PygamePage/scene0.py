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

        # Game over text
        self.game_over_text = gb_setting.FONT_GAME_OVER.render('GAME OVER', True, (255, 255, 255))
        self.restart_text = gb_setting.FONT_PRESS_SPACE.render('Press Space Bar to Restart', True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect()
        self.restart_rect = self.restart_text.get_rect()
        self.screen_fill = pygame.Surface((gb_var.SURFACE.get_width(), gb_var.SURFACE.get_height()))
        self.screen_fill.fill((0, 0, 0))
        self.screen_fill.set_alpha(128)
        self.screen_fill_rect = self.screen_fill.get_rect()

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

        if self.P1.is_dead:
            self.game_over_rect.center = (gb_var.SURFACE.get_width() // 2, gb_var.SURFACE.get_height() // 2)
            self.restart_rect.center = (gb_var.SURFACE.get_width() // 2, gb_var.SURFACE.get_height() // 2 + 25)
            gb_var.SURFACE.blit(self.screen_fill, self.screen_fill_rect)
            gb_var.SURFACE.blit(self.game_over_text, self.game_over_rect)
            gb_var.SURFACE.blit(self.restart_text, self.restart_rect)

        pygame.display.update()
        gb_var.FPS.tick(gb_setting.MAXFPS)
