""" TODO """

import arcade


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
