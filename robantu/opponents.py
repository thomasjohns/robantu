""" TODO """

import arcade

from .entities import Entity


class Opponent(Entity):

    def __init__(self, x, y, robantu):
        super().__init__(x, y)
        self.robantu = robantu


class Rock(Opponent):

    # def __init__(self, x, y):
    #     super().__init__(x, y)

    def update(self):
        pass

    def draw():
        pass
    