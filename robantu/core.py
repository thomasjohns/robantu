""" The main game window class and a method to start the game. """

import arcade
import json

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .rooms import HomeRoom
from .robots import Robantu


class RobantuWindow(arcade.Window):
    """ Main game window class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.state = {
            'room': HomeRoom,
            'health': 10,
            'entities': [Robantu],
        }

    def update(self):
        for entity in self.state['entities']:
            entity.update()
        self.state['room'].update()

    def on_draw(self):
        arcade.start_render()
        self.state['room'].draw()
        for entity in self.state['entities']:
            if entity.is_alive:
                entity.draw()

    def on_key_press(self):
        pass

    def on_key_release(self):
        pass

    def save_game(self):
        """ Save game state to file. """
        with open('saved_state.json', 'w') as f:
            json.load(self.state, f)


def run():
    window = RobantuWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
