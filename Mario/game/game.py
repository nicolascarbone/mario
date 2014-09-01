__author__ = 'nico'

from screen.screen import Screen
import pygame as pg


class Game(object):

    def __init__(self):
        self.screen = Screen()
        self.done = False

    def start_game(self):
        self.screen.initial_screen()
        while not self.done:
            self.events()
            # pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            else:
                self.keys = pg.key.get_pressed()

    def next_level(self):
        pass

    def quit_game(self):
        pass