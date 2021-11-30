import random
from game.constants import constants
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
        
        pass