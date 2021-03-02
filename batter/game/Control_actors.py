"""
Jeff
"""
from game import constants
from game.action import Action


class ControlActorsAction(Action):
    """
    The purpose of this class is to translate user input into an executable action.

    Params:
        class Action
    """
    def __init__(self, input_service):
        """
        The constructor method.

        Params:
            input_service (InputService) an instance of InputService.
        """
        super().__init__()
        self._input_service = input_service

    def execute(self, cast, screen):
        """
        The purpose of this method is to execute the actions for the given actors.

        Params:
            cast (dictionary)
        """
        direction = self._input_service.get_direction(screen)
        paddle = cast["paddle"][0]
        paddle.set_position(direction)
