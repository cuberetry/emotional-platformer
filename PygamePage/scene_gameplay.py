import sys

from InstanceModel.System.spr_tilemap import *
from InstanceModel.System.spr_camera import *
from InstanceModel.spr_player import *
from InstanceModel.System.spr_boundary import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr
from InstanceModel.Environment.spr_particle_emitter import *


class GameplayScene:
    def __init__(self, stage_filename):
        for spr in gb_spr.all_sprites.sprites():
            spr.kill()
            del spr

        self.stage_filename = stage_filename
        self.P1 = Player()
        self.fire_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.fire_timer, 40)

        # Load stage
        self.scene_map = TileMap(gb_setting.ROOT_PATH + "/StageData/" + self.stage_filename)
        self.P1.rect.x, self.P1.rect.y = self.scene_map.start_x, self.scene_map.start_y
        gb_var.CHECKPOINT = [self.scene_map.start_x, self.scene_map.start_y]
        self.particle = ParticleEmitter()

        self.boundary_map = BoundaryMap(gb_setting.ROOT_PATH + "/StageData/" + self.stage_filename)
        self.boundary = Boundary(self.P1, self.boundary_map)

        self.camera = Camera(self.P1, self.boundary_map)
        self.follow = Follow(self.camera, self.P1)
        self.border = Border(self.camera, self.P1)
        self.auto = Auto(self.camera, self.P1)
        self.camera.set_method(self.border)

        # Game over text
        self.game_over_text = gb_setting.FONT_GAME_OVER.render('GAME OVER', True, (255, 255, 255))
        self.restart_text = gb_setting.FONT_PRESS_SPACE.render('Press Space Bar to Restart', True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect()
        self.restart_rect = self.restart_text.get_rect()

        # Stage complete text
        self.stage_complete_text = gb_setting.FONT_GAME_OVER.render('STAGE COMPLETED!', True, (255, 255, 255))
        self.congrats_text = gb_setting.FONT_PRESS_SPACE.render('Press Space Bar to Return to Main Menu', True, (255, 255, 255))
        self.stage_complete_rect = self.stage_complete_text.get_rect()
        self.congrats_rect = self.congrats_text.get_rect()

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
            if event.type == self.fire_timer:
                for p in gb_spr.fire_sprites:
                    if r.randint(0, 100) < 20:
                        self.particle.add_particles(p.rect.x - self.camera.offset.x,
                                                    p.rect.y - self.camera.offset.y,
                                                    1, 'Smoke')
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        gb_var.SURFACE.fill((0, 0, 0))
        if gb_var.IS_PAUSING:
            return

        if self.P1.reached_goal:
            self.stage_complete_rect.center = (gb_var.SURFACE.get_width() // 2, gb_var.SURFACE.get_height() // 2)
            self.congrats_rect.center = (gb_var.SURFACE.get_width() // 2, gb_var.SURFACE.get_height() // 2 + 25)
            gb_var.SURFACE.blit(self.screen_fill, self.screen_fill_rect)
            gb_var.SURFACE.blit(self.stage_complete_text, self.stage_complete_rect)
            gb_var.SURFACE.blit(self.congrats_text, self.congrats_rect)

        self.particle.emit()
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

    def restart(self):
        for entity in gb_spr.all_sprites:
            entity.kill()
        gb_var.CUR_SCENE = GameplayScene(self.stage_filename)
        del self
