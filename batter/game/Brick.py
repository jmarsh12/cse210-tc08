# Craig
from game.actor import Actor


class Brick(Actor):
    def __init__(self):
        super().__init__()
        self.set_position()
        self.set_velocity(0, 0)
        self._text = '*'


    def set_position(self, point):
        self._position = point

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity