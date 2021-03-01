# Craig
from game.actor import Actor


class Brick(Actor):
    def __init__(self):
        super().__init__()
        self._velocity = (0, 0)
        self._text = '*'
        self._position = (0, 0)

    def set_position(self, point):
        self._position = point

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity
