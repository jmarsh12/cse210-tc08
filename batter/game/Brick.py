"""
Craig
"""
from game.actor import Actor
from game.point import Point


class Brick(Actor):
    def __init__(self, x, y):
        super().__init__()
        point = Point(x, y)
        self.set_position(point)
        self.set_velocity(Point(0, 0))
        self.set_text('*')
