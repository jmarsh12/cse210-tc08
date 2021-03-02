"""
Craig
"""
from game.actor import Actor
from game import constants
from random import randint
from game.point import Point


class Ball(Actor):
    def __init__(self):
        super().__init__()
        #constant = Constants()
        position = Point(int(constants.MAX_X / 2), int(constants.MAX_Y / 2))
        velocity = Point(1, -1)
        self.set_position(position)
        self.set_velocity(velocity)  # sets self.velocity randomly between -4 and 4
        self.set_text('O')
    