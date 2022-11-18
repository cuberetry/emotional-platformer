import sys
from InstanceModel.spr_platform import *
from InstanceModel.spr_player import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr

pygame.init()

FramePerSec = pygame.time.Clock()

display_surface = pygame.display.set_mode((gb_setting.WIDTH, gb_setting.HEIGHT))
pygame.display.set_caption("Emotional Platformer")

P1 = Player()
platform_1 = Platform(gb_setting.WIDTH, gb_setting.HEIGHT)

gb_spr.all_sprites.add(P1)
gb_spr.all_sprites.add(platform_1)

gb_spr.env_sprites.add(platform_1)

while True:
    P1.move()
    P1.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display_surface.fill((0, 0, 0))

    for entity in gb_spr.all_sprites:
        display_surface.blit(entity.surf, entity.rect)
    pygame.display.update()
    FramePerSec.tick(gb_setting.FPS)
