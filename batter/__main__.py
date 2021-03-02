import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors import ControlActorsAction
from game.draw_actors import DrawActorsAction
from game.handle_collisions import HandleCollisionsAction
from game.move_actors import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

from game.Paddle import Paddle
from game.Ball import Ball
from game.Brick import Brick

def main(screen):
    # create the cast {key: tag, value: list}
    cast = {}
    paddle = Paddle()
    cast["paddle"] = [paddle]
    
    cast["ball"] = []
    
    ball = Ball()
    cast["ball"] = [ball]
    
    cast["bricks"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            brick = Brick(x, y)
            cast["bricks"].append(brick)
    # create the script {key: tag, value: list}
    script = {}
    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]
    # start the game
    director = Director(cast, script)
    director.start_game()
Screen.wrapper(main)