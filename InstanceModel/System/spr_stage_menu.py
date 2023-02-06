import pygame_menu as pgm
from GlobalVariable import game_var as gb_var
from GlobalVariable import game_setting as gb_setting
import os
import functools as ft
import PygamePage.scene_main_menu as smm
import PygamePage.scene_gameplay as sg


class StageMenu:
    def __init__(self, prev_menu=None):
        self.prev_menu = prev_menu
        self.menu = pgm.Menu('Pause Menu', gb_setting.WIDTH, gb_setting.HEIGHT, theme=pgm.themes.THEME_DARK)
        self.menu.add.button('Return', self.game_continue)
        stage_lst = next(os.walk(gb_setting.ROOT_PATH + "/StageData/"))[2][::-1]
        for stages in stage_lst:
            stage = stages[:stages.index('.')]
            self.menu.add.button(stages[:stages.index('.')], ft.partial(self.game_stage, stage=stage))
        self.menu.add.button('Quit', pgm.events.EXIT)
        self.menu.disable()

    def activate_menu(self):
        self.menu.enable()

    def mainloop(self):
        self.menu.mainloop(gb_var.SURFACE, disable_loop=True)

    def game_continue(self):
        self.prev_menu.activate_menu()
        self.menu.disable()

    def game_stage(self, stage):
        path = stage + '.csv'
        self.prev_menu.activate_menu()
        self.menu.disable()
        if not isinstance(gb_var.CUR_SCENE, smm.MainMenuScene):
            gb_var.IS_PAUSING = False
            gb_var.CUR_SCENE.stage_filename = path
            gb_var.CUR_SCENE.restart()
        else:
            gb_var.CUR_SCENE = sg.GameplayScene(path)

    def is_activated(self):
        return self.menu.is_enabled()
