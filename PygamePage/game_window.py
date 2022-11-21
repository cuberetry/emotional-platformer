import GlobalVariable.game_setting as gb_setting
import GlobalVariable.game_var as gb_var
import pygame
from PygamePage import scene_main_menu


class MainPygameWindow:
    def __init__(self):
        pygame.init()
        gb_var.FPS = pygame.time.Clock()
        gb_var.SURFACE = pygame.display.set_mode((gb_setting.WIDTH, gb_setting.HEIGHT))
        pygame.display.set_caption("Emotional Platformer")
        gb_var.CUR_SCENE = scene_main_menu.Scene()
