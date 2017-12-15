""" TODO """

import math
import itertools
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
        self.color = arcade.color.SALMON
        self.angle = 0
        self.movement_speed = 10
        self.eye_size = 5  # in pixels
        self.beam_length = 45
        self.beam_width = 5 # in pixels
        self.using_beam = False
        self.beam_color_cycle = itertools.cycle([
            arcade.color.RED,
            arcade.color.PINK,
            arcade.color.ORANGE,
            arcade.color.PURPLE,
        ])

        # TODO ideas to render into text and game logic later
        # self.health = {
        #     'current': 15,
        #     'max': 15,
        # }
        # self.energy = {
        #     'current': 25,
        #     'max': 25,
        # }

    def update(self, is_allowable_region):
        new_x = self.x + self.dx
        new_y = self.y + self.dy
        if is_allowable_region(new_x, new_y, self.width, self.height):
            self.x = new_x
            self.y = new_y

    def _draw_body(self):
        arcade.draw_rectangle_filled(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color,
        )

    def _draw_eyes(self):
        # left eye
        arcade.draw_point(
            self.x + 0.8 * self.width // 2 * math.cos(math.pi / 6 + self.angle),
            self.y + 0.8 * self.height // 2 * math.sin(math.pi / 6 + self.angle),
            arcade.color.BLACK,
            self.eye_size,
        )
        # right eye
        arcade.draw_point(
            self.x + 0.8 * self.width // 2 * math.cos(-math.pi / 6 + self.angle),
            self.y + 0.8 * self.height // 2 * math.sin(-math.pi / 6 + self.angle),
            arcade.color.BLACK,
            self.eye_size,
        )

    def _draw_beam_handle(self):
        pass

    def _draw_beam(self):
        if self.using_beam:
            beam_color = next(self.beam_color_cycle)
            arcade.draw_line(self.x, self.y, self.x, self.y + self.beam_length,
                             beam_color, self.beam_width)

    def _draw_blaster(self):
        pass

    def draw(self):
        self._draw_body()
        self._draw_eyes()
        self._draw_beam_handle()
        self._draw_beam()
        self._draw_blaster()

    def handle_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.dy = self.movement_speed
        elif symbol == arcade.key.S:
            self.dy = -self.movement_speed
        elif symbol == arcade.key.A:
            self.dx = -self.movement_speed
        elif symbol == arcade.key.D:
            self.dx = self.movement_speed

        if symbol == arcade.key.O:
            self.angle = math.pi / 2
        elif symbol == arcade.key.L:
            self.angle = 3 * math.pi / 2
        elif symbol == arcade.key.K:
            self.angle = math.pi
        elif symbol == arcade.key.SEMICOLON:
            self.angle = 0

        if symbol == arcade.key.J:
            self.using_beam = True

    def handle_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.dy = 0
        elif symbol == arcade.key.A or symbol == arcade.key.D:
            self.dx = 0

        if symbol == arcade.key.J:
            self.using_beam = False
