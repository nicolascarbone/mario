__author__ = 'nico'


import os
import pygame as pg
from resources import Resources
# from resources.tools.tools import Tools

class Screen(object):

    def __init__(self):
        self.height = 600
        self.width = 800
        self.screen_size = (self.width, self.height)
        # Tools().load_pg(self.screen_size)
        pg.init()
        pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
        pg.display.set_caption('Mario!')
        pg.display.set_mode(self.screen_size)
        self.resources = Resources()

    def initial_screen(self):


        path = os.path.join('resources/images/', 'item_objects.png')
        img = self.resources.load_resource(path)

        cursor = pg.sprite.Sprite()
        dest = (220, 358)
        cursor.image, cursor.rect = self.get_image(24, 160, 8, 8, dest, img)
        cursor.state = '1 Player'

        surface = pg.display.get_surface()
        surface.blit(cursor.image, cursor.rect)

        pg.display.update()

        # screen = pg.display.set_mode(self.screen_size)
        # screen_rect = screen.get_rect()
        # viewport = screen.get_rect(bottom=screen_rect.bottom)




    def get_image(self, x, y, width, height, dest, sprite_sheet):
        """Returns images and rects to blit onto the screen"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((255, 0, 220))
        image = pg.transform.scale(image,
                               (int(rect.width * 2.5),
                                int(rect.height * 2.5)))

        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return (image, rect)
