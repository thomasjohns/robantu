""" TODO """

import math
import itertools
import arcade

from .constants import MENU_WIDTH
from .entities import Entity


class Robot(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_alive = True


class EnergyBall(Entity):
    pass


class Robantu(Robot):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx = 0
        self.dy = 0
        self.width = 50
        self.height = 50
        self.diagonal_length = math.sqrt(self.width ** 2 + self.height ** 2)
        self.color = arcade.color.SALMON
        self.angle = 0
        self.movement_speed = 10

        self.eye_size = 5
        self.left_eye_x, self.left_eye_y = self._get_left_eye_coords()
        self.right_eye_x, self.right_eye_y = self._get_right_eye_coords()

        self.beam_handle_x, self.beam_handle_y = self._get_beam_handle_coords()
        self.beam_handle_width = 9
        self.beam_handle_height = 9

        self.beam_length = 60
        self.beam_width = 5
        self.beam_coords = self._get_beam_coords()
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

    def _get_left_eye_coords(self):
        return [
            self.x + 0.8 * self.width // 2 * math.cos(math.pi / 6 + self.angle),
            self.y + 0.8 * self.height // 2 * math.sin(math.pi / 6 + self.angle),
        ]

    def _get_right_eye_coords(self):
        return [
            self.x + 0.8 * self.width // 2 * math.cos(-math.pi / 6 + self.angle),
            self.y + 0.8 * self.height // 2 * math.sin(-math.pi / 6 + self.angle),
        ]

    def _get_beam_handle_coords(self):
        return [
            self.x + self.diagonal_length / 2 * math.cos(self.angle + math.pi / 4),
            self.y + self.diagonal_length / 2 * math.sin(self.angle + math.pi / 4),
        ]

    def _get_beam_coords(self):
        coords = {}
        if self.angle == 0:  # facing right
            coords['start_x'] = self.beam_handle_x + self.beam_handle_width / 2
            coords['start_y'] = self.beam_handle_y
            coords['end_x'] = (
                self.beam_handle_x +
                self.beam_handle_width / 2 +
                self.beam_length
            )
            coords['end_y'] = self.beam_handle_y
        elif self.angle == math.pi / 2:  # facing up
            coords['start_x'] = self.beam_handle_x
            coords['start_y'] = self.beam_handle_y + self.beam_handle_height / 2
            coords['end_x'] = self.beam_handle_x
            coords['end_y'] = (
                self.beam_handle_y +
                self.beam_handle_height / 2 +
                self.beam_length
            )
        elif self.angle == math.pi:  # facing left
            coords['start_x'] = self.beam_handle_x - self.beam_handle_width / 2
            coords['start_y'] = self.beam_handle_y
            coords['end_x'] = max([
                self.beam_handle_x - self.beam_handle_width / 2 - self.beam_length,
                MENU_WIDTH
            ])
            coords['end_y'] = self.beam_handle_y
        else:  # facing down
            coords['start_x'] = self.beam_handle_x
            coords['start_y'] = self.beam_handle_y - self.beam_handle_height / 2
            coords['end_x'] = self.beam_handle_x
            coords['end_y'] = (
                self.beam_handle_y -
                self.beam_handle_height / 2 -
                self.beam_length
            )
        return coords

    def beam_hits(self, x, y, entity_radius):
        """
        Determine if an entity with location (x, y) and radius: entitiy_radius
        intersects with Robantu's beam.
        """
        y_is_within = x_is_within = False
        if self.angle == 0 or self.angle == math.pi:  # horizontal beam
            y_is_within = abs(self.beam_coords['start_y'] - y) <= entity_radius
            if self.angle == 0:  # beam moves from left to right
                x_is_within = (
                    x + entity_radius > self.beam_coords['start_x'] and
                    x - entity_radius < self.beam_coords['end_x']
                )
            else:  # beam moves from right to left
                x_is_within = (
                    x + entity_radius > self.beam_coords['end_x'] and
                    x - entity_radius < self.beam_coords['start_x']
                )
        else:  # vertical beam
            if self.angle == math.pi / 2:  # beam moves up
                y_is_within = (
                    y + entity_radius > self.beam_coords['start_y'] and
                    y - entity_radius < self.beam_coords['end_y']
                )
            else:  # beam moves down
                y_is_within = (
                    y + entity_radius > self.beam_coords['end_y'] and
                    y - entity_radius < self.beam_coords['start_y']
                )
            x_is_within = abs(self.beam_coords['start_x'] - x) <= entity_radius
        return y_is_within and x_is_within

    def update(self, is_allowable_region):
        new_x = self.x + self.dx
        new_y = self.y + self.dy
        if is_allowable_region(new_x, new_y, self.width, self.height):
            self.x = new_x
            self.y = new_y
        self.left_eye_x, self.left_eye_y = self._get_left_eye_coords()
        self.right_eye_x, self.right_eye_y = self._get_right_eye_coords()
        self.beam_handle_x, self.beam_handle_y = self._get_beam_handle_coords()
        self.beam_coords = self._get_beam_coords()

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
            self.left_eye_x,
            self.left_eye_y,
            arcade.color.BLACK,
            self.eye_size,
        )
        # right eye
        arcade.draw_point(
            self.right_eye_x,
            self.right_eye_y,
            arcade.color.BLACK,
            self.eye_size,
        )

    def _draw_beam_handle(self):
        arcade.draw_rectangle_filled(
            self.beam_handle_x,
            self.beam_handle_y,
            self.beam_handle_width,
            self.beam_handle_height,
            arcade.color.AZURE_MIST,
        )

    def _draw_beam(self):
        if self.using_beam:
            beam_color = next(self.beam_color_cycle)
            arcade.draw_line(
                **self.beam_coords,
                color=beam_color,
                border_width=self.beam_width
            )

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
