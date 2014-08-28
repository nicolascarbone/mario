__author__ = 'nico'


import pygame as pg


class Resources(object):

    def load_resource(self, path):
        img = pg.image.load(path)
        if img.get_alpha():
            img = img.convert_alpha()
        else:
            img = img.convert()
            colorkey = (255,0,255)
            img.set_colorkey(colorkey)

        return img