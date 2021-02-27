"""
Jeff
"""


class Point:
    """
    The purpose of this class is to represent a distance from the origin (0, 0).
    """
    def __init__(self, x, y):
        """
        The constructor method
        """
        self._x = x
        self._y = y

    def is_equal(self, other):
        """
        TThe is_equal method checks if the position of the ball is equal to the position of the paddle and
        the bricks.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """
        This returns the horizontal distance.
        """
        return self._x

    def get_y(self):
        """
        This returns the vertical distance.
        """
        return self._y

    def is_zero(self):
        """
        Checks if the point of the paddle is zero.

        Returns a boolean; if x = 0 and y = 0 it's True, and False if otherwise.
        """
        return self._x == 0 and self._y == 0

    def reverse(self):
        """
        This allows for the actors to be reversed.
        """
        x = self._x * -1
        y = self._y * -1
        return Point(x, y)
