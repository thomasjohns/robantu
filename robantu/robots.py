""" TODO """

import arcade

from .entities import Entity


class Robot(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_alive = True


class Robantu(Robot):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx = 0
        self.dy = 0
        self.width = 50
        self.height = 50
        self.color = arcade.color.AERO_BLUE
        self.angle = 0
        self.movement_speed = 10

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

    def handle_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.dy = self.movement_speed
        elif symbol == arcade.key.DOWN:
            self.dy = -self.movement_speed
        elif symbol == arcade.key.LEFT:
            self.dx = -self.movement_speed
        elif symbol == arcade.key.RIGHT:
            self.dx = self.movement_speed

    def handle_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.dy = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.dx = 0
