"""
Moon
"""
import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"] # there are 280 brick? in cast['brick']
        paddle = cast["paddle"][0]
        #artifacts = cast["artifact"]
        #marquee.set_text("")
        velocity = ball.get_velocity()
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text("")     
                velocity.reverse()      # reverse the direction of ball. 
        position = ball.get_position()
        if position.get_x() == 0 or position.get_x() == constants.MAX_X or position.get_y() == 0:  
            velocity.reverse() 
        
        if position.get_y() == constants.MAX_Y - 1:
            for i in range(paddle.get_position().get_x(), paddle.get_position().get_x()+10):
                if position.get_x() == i:
                    velocity.reverse()
        
        if position.get_y() == constants.MAX_Y: # game over?
            pass