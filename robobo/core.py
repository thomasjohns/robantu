""" The main game window class and a method to start the game. """

import arcade

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Robobo(arcade.Window):
    """ Main game window class. """

    def __init__(self, width, height):
        super().__init__(width, height)


def run():
    window = Robobo(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
