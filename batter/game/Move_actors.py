"""
Bryson
"""
from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """
        Executes the action using the given actors.
        """

    
    def execute(self, cast):
        """Loops through all of the actors within cast and
        Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        #velocity.reverse()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        if actor.get_text() == "===========":
            if x1 == constants.MAX_X - 8:
                if x2 == -4:
                    x = 1 + (x1 + x2 - 1) # % (constants.MAX_X - 1)
                    y = 1 + (y1 + y2 - 1) # % (constants.MAX_Y - 1)
                    position = Point(x, y)
                else:    
                    position = Point(x1, y1)
            elif x1 == 0:
                if x2 == 4:
                    x = 1 + (x1 + x2 - 1) # % (constants.MAX_X - 1)
                    y = 1 + (y1 + y2 - 1) # % (constants.MAX_Y - 1)
                    position = Point(x, y)
                else: 
                    position = Point(x1, y1)
            else:
                x = 1 + (x1 + x2 - 1) # % (constants.MAX_X - 1)
                y = 1 + (y1 + y2 - 1) # % (constants.MAX_Y - 1)
                position = Point(x, y)
        else:
            x = 1 + (x1 + x2 - 1) # % (constants.MAX_X - 1)
            y = 1 + (y1 + y2 - 1) # % (constants.MAX_Y - 1)
            position = Point(x, y)
        actor.set_position(position)
