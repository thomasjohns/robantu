""" TODO """

import arcade


class Robot(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = True

    def update(self):
        pass

    def draw(self):
        pass


class Robantu(Robot):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx = 0
        self.dy = 0
        self.width = 50
        self.height = 50
        self.color = arcade.color.AERO_BLUE
        self.angle = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        arcade.draw_rectangle_filled(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color,
            self.angle,
        )
