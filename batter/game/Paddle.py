# Craig
from game.actor import Actor
from game import constants


class Paddle(Actor):
    def __init__(self):
        super().__init__()
        self._position = ((constants.MAX_X / 2), constants.MAX_Y)
        self._text = '=========='

    def set_position(self, position):
        self._position = position
        return self._position

    def get_position(self):
        return self._position

    def get_right_side_paddle(self):
        x1 = self._position.get_x() + (len(self._text))
        y1 = self._position.get_y()
        right_side_paddle = (x1, y1)
        return right_side_paddle