""" The main game window class and a method to start the game. """

import arcade

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .rooms import HomeRoom
from .robots import Robantu


class State(object):

    def __init__(self, room, entities):
        self.room = room
        self.entities = entities

    def load_game_state(self):
        # TODO
        pass

    def save_game_state(self):
        """ Save game state to file. """
        # TODO
        pass


class RobantuWindow(arcade.Window):
    """ Main game window class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        home_room = HomeRoom()
        self.state = State(
            room=home_room,
            entities=[Robantu(home_room.start_x, home_room.start_y)],
        )

    def update(self, dt):
        for entity in self.state.entities:
            entity.update(self.state.room.is_allowable_region_in_room)
        # self.state.room.update()

    def on_draw(self):
        arcade.start_render()
        # self.state.room.draw()
        for entity in self.state.entities:
            if entity.is_alive:
                entity.draw()

    def on_key_press(self, symbol, modifiers):
        for entity in self.state.entities:
            entity.handle_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        for entity in self.state.entities:
            entity.handle_key_release(symbol, modifiers)


def run():
    window = RobantuWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
