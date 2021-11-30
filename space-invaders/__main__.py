import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
from game.game_score import Gamescore

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    # create the script {key: tag, value: list}
    script = {}

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)