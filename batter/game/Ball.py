"""
Craig
"""
from game.actor import Actor
from game import constants
from random import randint
from game.point import Point


class Ball(Actor):
    """An actor in the batter game. Ball inherits from Actor.

        Attributes: Point: the position on the screen
                    Velocity: the speed it is moving; set randomly at the beginning
                    Text: visual representation of the ball
                    """

    def __init__(self):
        """Class constructor"""

        super().__init__()
        position = Point(int(constants.MAX_X / 2), int(constants.MAX_Y / 2))
        x = randint(-4, 4)  # sets x to a random int between -4 and 4
        y = randint(-3, 3)  # sets y to a random int between -3 and 3
        if x == 0:
            x = 1  # makes sure x does not equal 0
        if y == 0:
            y = 1  # makes sure y does not equal 0
        velocity = Point(x, y)
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_text('O')
