import sys
from InstanceModel.spr_platform import *
from InstanceModel.spr_player import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr


class Scene:
    def __init__(self):
        self.P1 = Player()
        self.platform_1 = Platform(gb_setting.WIDTH, gb_setting.HEIGHT)

    def mainloop(self):
        self.P1.move()
        self.P1.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        gb_var.SURFACE.fill((0, 0, 0))

        for entity in gb_spr.all_sprites:
            gb_var.SURFACE.blit(entity.surf, entity.rect)
        pygame.display.update()
        gb_var.FPS.tick(gb_setting.MAXFPS)
