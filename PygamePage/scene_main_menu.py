import pygame_menu as pgm
from GlobalVariable import game_var as gb_var
from GlobalVariable import game_setting as gb_setting
from PygamePage import scene_gameplay


class MainMenuScene:
    def __init__(self):
        # Create a simple menu with buttons
        self.is_activated = True
        self.menu = pgm.Menu('Emotional Platformer', gb_setting.WIDTH, gb_setting.HEIGHT, theme=pgm.themes.THEME_DARK)
        self.menu.add.button('Play', self.start_game)
        self.menu.add.button('Select Stage', self.select_stage)
        self.menu.add.button('Quit', pgm.events.EXIT)

    def activate_menu(self):
        self.menu.enable()
        self.is_activated = True

    def mainloop(self):
        if self.is_activated:
            self.menu.mainloop(gb_var.SURFACE, disable_loop=True)
        else:
            gb_var.STAGE_SELECT.menu.mainloop(gb_var.SURFACE, disable_loop=True)

    def start_game(self):
        self.menu.disable()
        gb_var.CUR_SCENE = scene_gameplay.GameplayScene('stage01.csv')

    def select_stage(self):
        self.menu.disable()
        self.is_activated = False
        gb_var.STAGE_SELECT.prev_menu = self
        gb_var.STAGE_SELECT.activate_menu()
