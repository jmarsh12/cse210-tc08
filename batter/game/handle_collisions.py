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
        bricks = cast["bricks"] # there are 280 brick? in cast['brick']
        paddle = cast["paddle"][0]
        velocity = ball.get_velocity()
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                if brick.get_text() == "*":
                    brick.set_text("")     
                    ball.set_velocity(velocity.reverse_y())    # reverse the direction of ball. 
        
        position = ball.get_position()
         
        
        if (position.get_y() == constants.MAX_Y - 2):
            # if position.get_x() == 0 or position.get_x() == constants.MAX_X:
            #     ball.set_velocity(velocity.reverse())
                
            # else:
            #     ball.set_velocity(velocity.reverse_y())

            for i in range(paddle.get_position().get_x(), paddle.get_position().get_x()+11):
                if position.get_x() == i and (position.get_x() == 1 or position.get_x() == constants.MAX_X ):
                    ball.set_velocity(velocity.reverse())
                    #ball.set_velocity(velocity.reverse_y())
                    
                elif position.get_x() == i:
                    ball.set_velocity(velocity.reverse_y())

        elif position.get_y() == 1:
            if position.get_x() == 0 or position.get_x() == constants.MAX_X: 
            
                ball.set_velocity(velocity.reverse())  
                # ball.set_velocity(velocity.reverse_y()) 
            else:
                ball.set_velocity(velocity.reverse_y()) 
        
        elif position.get_x() == 0 or position.get_x() == constants.MAX_X: 
            ball.set_velocity(velocity.reverse_x())  
        
    
        if position.get_y() == constants.MAX_Y: # game over?
            pass
