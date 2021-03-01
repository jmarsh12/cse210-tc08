# Craig


class Actor:

    def __init__(self):
        self._position = (0, 0)
        self._velocity = (0, 0)
        self._text = ''

    def is_collision(self, actor1, actor2):
        if actor1.get_position == actor2.get_position:
            return True
        else:
            return False