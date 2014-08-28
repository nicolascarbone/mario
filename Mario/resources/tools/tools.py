__author__ = 'nico'

import pygame as pg

class Tools(object):

    def load_pg(self, screen_size):
        pg.init()
        pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
        pg.display.set_caption('Nico!')
        pg.display.set_mode(screen_size)