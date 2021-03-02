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

        # cast["brick"] = []
        # for x in range(5, 75):
        #     for y in range(2, 6):
        #         position = Point(x, y)
        #         brick = Actor()
        #         brick.set_text("*")
        #         brick.set_position(position)
        #         cast["brick"].append(brick)
    
    


    # def set_position(self, point):
    #     self._position = point

    # def get_position(self):
    #     return self._position

    # def get_velocity(self):
    #     return self._velocity