"""
Craig
"""
from game.actor import Actor
from game.point import Point


class Brick(Actor):
    """An actor in the batter game. Brick inherits from Actor.

    Attributes: Point: the position on the screen
                Velocity: the speed it is moving; always set to zero
                Text: visual representation of the brick
                """

    def __init__(self, x, y):
        """Class constructor"""

        super().__init__()
        point = Point(x, y)
        self.set_position(point)
        self.set_velocity(Point(0, 0))
        self.set_text('*')
