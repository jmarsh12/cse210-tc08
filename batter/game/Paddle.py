"""
Craig
"""
from game.actor import Actor
from game import constants
from game.point import Point


class Paddle(Actor):
    """An actor in the batter game. Paddle inherits from Actor.

        Attributes: Point: the position on the screen
                    Velocity: the speed it is moving; initialized to zero
                    Text: visual representation of the brick
                    """

    def __init__(self):
        """Class constructor"""

        super().__init__()
        position = Point(int(constants.MAX_X / 2), constants.MAX_Y - 1)
        self.set_position(position)
        self.set_velocity(Point(0, 0))
        self.set_text('===========')
