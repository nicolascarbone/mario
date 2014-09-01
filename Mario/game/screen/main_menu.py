

import os
import pygame as pg
from resources import Resources

# create interface
class MainMenu(object):

    def __init__(self):
        self.resources = Resources()


    def load(self):
        path = os.path.join('resources/images/', 'item_objects.png')
        img = self.resources.load_resource(path)

        cursor = pg.sprite.Sprite()
        dest = (220, 358)
        cursor.image, cursor.rect = self.get_image(24, 160, 8, 8, dest, img)
        cursor.state = '1 Player'

        surface = pg.display.get_surface()
        surface.blit(cursor.image, cursor.rect)

        pg.display.update()


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
