"""
Bryson
"""
from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):

    
    def execute(self, cast):
        """Loops throught all of the actors within cast and 
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
        velocity. 
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        # x1 = position.get_x()
        # y1 = position.get_y()
        # x2 = velocity.get_x()
        # y2 = velocity.get_y()
