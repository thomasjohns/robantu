""" TODO """

import arcade

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_WIDTH


class Room():

    def update(self):
        pass

    def draw(self):
        pass

    def is_within_screen(self, x, y, width, height):
        return (
            (MENU_WIDTH + width // 2) < x < (SCREEN_WIDTH - width // 2) and
            (0 + height // 2) < y < (SCREEN_HEIGHT - height // 2)
        )

class HomeRoom(Room):

    def __init__(self):
        self.start_x = 500
        self.start_y = 500
        self.exit_zones = []  # some kind of area (collision points) which maps to a new room

    def is_allowable_region_in_room(self, x, y, width, height):
        return self.is_within_screen(x, y, width, height)
