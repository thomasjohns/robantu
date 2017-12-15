""" TODO """

import arcade

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Room():

    def update(self):
        pass

    def draw(self):
        pass


class HomeRoom(Room):

    def __init__(self):
        self.start_x = 500
        self.start_y = 500
        self.exit_zones = []  # some kind of area (collision points) which maps to a new room

    def is_allowable_region(self, x, y, width, height):
        # TODO: this could probably be added to the parent class room
        ### boundary method
        return (
            (0 + width // 2) < x < (SCREEN_WIDTH - width // 2) and
            (0 + height // 2) < y < (SCREEN_HEIGHT - height // 2)
        )
        ###
