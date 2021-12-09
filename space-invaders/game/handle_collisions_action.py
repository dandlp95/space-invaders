import random
from game import constants
from game.action import Action
from game.point import Point
from game.game_score import Gamescore
import sys
from asciimatics.screen import Screen
from time import sleep

class HandleCollisionsAction(Action):
    """Handles how the different actors will react when a collision
    is detected."""

    def __init__(self, screen, gamescore):
        self.screen = screen
        self._gamescore = gamescore

    def execute(self, cast):
        
        players_ship_position_x = cast["player_ship"][0].get_position().get_x()
        players_ship_position_y = cast["player_ship"][0].get_position().get_y()
        invaders = cast["invaders"]

        if cast["beams"]:
            beam_position_y = cast["beams"][0].get_position().get_y()
            beam_position_x = cast["beams"][0].get_position().get_x()
        
        # Removes invader if the beam touches the invader.
            for invader in invaders:
                invader_position_y = invader.get_position().get_y()
                if invader_position_y == beam_position_y:
                    invader_position_x = invader.get_position().get_x()
                    if invader_position_x == beam_position_x:
                        invaders.remove(invader)
                        # Removes beam upon coallision.
                        cast["beams"].pop(0)
                        self._gamescore.add_point(1)
        
        # Removes players ship upon impact.
        if cast["invader_beams"]:
            invaders_beams = cast["invader_beams"]
            for invader_beam in invaders_beams:
                invader_beam_position_y = invader_beam.get_position().get_y()
                if invader_beam_position_y == players_ship_position_y - 1:
                    invader_beam_position_x = invader_beam.get_position().get_x()
                    if players_ship_position_x <= invader_beam_position_x <= players_ship_position_x + 2:
                        cast["player_ship"].pop(0)

                



