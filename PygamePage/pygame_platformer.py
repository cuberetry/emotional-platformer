import sys
from InstanceModel.spr_platform import *
from InstanceModel.spr_camera import *
from InstanceModel.spr_player import *
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr

pygame.init()

FramePerSec = pygame.time.Clock()

display_surface = pygame.display.set_mode((gb_setting.WIDTH, gb_setting.HEIGHT))
pygame.display.set_caption("Emotional Platformer")

P1 = Player()
platform_1 = Platform(gb_setting.WIDTH, gb_setting.HEIGHT)

camera = Camera(P1)
follow = Follow(camera, P1)
border = Border(camera, P1)
auto = Auto(camera, P1)
camera.setmethod(border)


while True:
    P1.move()
    P1.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display_surface.fill((0, 0, 0))

    camera.scroll()
    for entity in gb_spr.all_sprites:
        display_surface.blit(entity.surf, (entity.rect.x - camera.offset.x, entity.rect.y - camera.offset.y))
    display_surface.blit(P1.surf, (P1.rect.x - camera.offset.x, P1.rect.y - camera.offset.y))

    # update window and display
    pygame.display.update()
    FramePerSec.tick(gb_setting.FPS)
