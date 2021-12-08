import random
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
from game.ship import Ship
from game.weapon import Weapon
from game import constants


def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    ship_position = Point(x, y)
    beam_velocity = Point(0, -1)
    player_ship = Ship()
    player_ship.set_position(ship_position)
    player_ship.set_beam_velocity(beam_velocity)
    player_ship.set_text("^")

    cast["player_ship"] = [player_ship]

    cast["invaders"] = []
    for x in range(20, 55,4):
        for y in range(2,6):
            ship_position = Point(x, y)
            beam_velocity = Point(0,1)
            invader = Ship()
            invader.set_position(ship_position)
            invader.set_text("(0)")
            invader.set_beam_velocity(beam_velocity)
            cast["invaders"].append(invader)
    
    cast["beams"] = []
    
    gamescore = Gamescore(len(cast["invaders"]))

    # create the script {key: tag, value: list}
    script = {}
    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    weapon = Weapon()
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(screen, gamescore)
    draw_actors_action = DrawActorsAction(output_service)
 
    
    script["input"] = [control_actors_action]
    script["update"] = [weapon, move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)