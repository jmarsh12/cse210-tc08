"""
Craig
"""
from game.actor import Actor
from game import constants
from game.point import Point


class Paddle(Actor):
    def __init__(self):
        super().__init__()
        #constant = Constants()
        position = Point(int(constants.MAX_X / 2), constants.MAX_Y - 1)
        self.set_position(position)
        self.set_velocity(Point(0, 0))
        self.set_text('===========')
        
        # x = int(constants.MAX_X / 2)
        # y = int(constants.MAX_Y - 1)
        # position = Point(x, y)
        # paddle = Actor()
        # paddle.set_text("===========")
        # paddle.set_position(position)
    
    

    # def get_position(self):
    #     return self._position

    # def get_right_side_paddle(self):
    #     x1 = self._position.get_x() + (len(self._text))
    #     y1 = self._position.get_y()
    #     right_side_paddle = (x1, y1)
    #     return right_side_paddle