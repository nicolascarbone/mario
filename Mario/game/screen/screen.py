__author__ = 'nico'


import pygame as pg
from main_menu import MainMenu


class Screen(object):

    def __init__(self):
        self.setup_screen()

    def setup_screen(self):
        self.height = 600
        self.width = 800
        self.screen_size = (self.width, self.height)
        pg.init()
        pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
        pg.display.set_caption('Mario!')
        pg.display.set_mode(self.screen_size)


    def main_menu(self):
        MainMenu().load()

