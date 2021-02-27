"""
Bryson
"""
class Action:
    """
    The class for anything proceedure or operation done within the game.
    This class contains the things that Actors do to change and interact
    within the game. All Action classes inherit Action.
    """

def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")