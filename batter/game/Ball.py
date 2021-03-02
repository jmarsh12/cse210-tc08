"""
Craig
"""
from game.actor import Actor
from game import constants
from random import randint
from game.point import Point
from game.actor import Actor
from game import constants
from random import randint


class Ball(Actor):
    def __init__(self):
        super().__init__()
        #constant = Constants()
        position = Point(int(constants.MAX_X / 2), int(constants.MAX_Y / 2))
        velocity = Point(1, -1)
        self.set_position(position)
        self.set_velocity(velocity)  # sets self.velocity randomly between -4 and 4
        self.set_text('O')
    

        #position = Point(x, y)
        # velocity = Point(1, -1)
        # ball = Actor()
        # ball.set_text("@")
        # ball.set_position(position)
        # ball.set_velocity(velocity)
        # cast["ball"] = [ball]

    # def __set_velocity(self):
    #     x = randint(-4, 4)
    #     y = 1
    #     if x == 0:
    #         x += 1
    #     self.velocity = (x, y)

    # def get_position(self):
    #     return self._position

    # def get_velocity(self):
    #     return self._velocity
        self._position = ((constants.MAX_X / 2), (constants.MAX_Y - 1))
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
