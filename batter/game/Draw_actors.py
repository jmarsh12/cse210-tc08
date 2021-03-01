"""
Jeff
"""
from game.action import Action


class DrawActorsAction(Action):
    """
    The purpose of this class is to draw each of the actions of the actors in the cast (paddle, ball, brick)
    """

    def __init__(self, output_service):
        """
        The constructor method.

        Params:
            output_service (OutputService) an instance of OutputService.
        """
        super().__init__()
        self._output_service = output_service

    def execute(self, cast):
        """
        The execute method is meant to actually execute the actions for the actors to perform.

        Params:
            cast (dictionary)
        """
        self._output_service.clear_screen()

        for actor in cast.values():
            self._output_service.draw_actors(actor)
        self._output_service.flush_buffer()
