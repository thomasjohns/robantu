""" TODO """


class Entity(object):
    
    def __init__(self, x, y, is_alive=True):
        self.x = x
        self.y = y
        self.is_alive = is_alive

    def update(self, is_allowable_region_in_room):
        pass

    def draw(self):
        pass

    def handle_key_press(self, symbol, modifiers):
        pass

    def handle_key_release(self, symbol, modifiers):
        pass
