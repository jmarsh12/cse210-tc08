# Craig
from game.actor import Actor
from game.constants import Constants
from random import randint


class Ball(Actor):
    def __init__(self):
        super().__init__()
        constant = Constants()
        self._position = ((constant.MAX_X / 2), (constant.MAX_Y - 1))
        self.__set_velocity()  # sets self.velocity randomly between -4 and 4
        self._text = 'O'

    def __set_velocity(self):
        x = randint(-4, 4)
        y = 1
        if x == 0:
            x += 1
        self.velocity = (x, y)

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity