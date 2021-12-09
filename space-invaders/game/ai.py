from game.ship import Ship
from game.point import Point
from game import constants
import random

class Ai:
    """Makes automatic movements for NPC"""

    def __init__(self):
        self._move_left = Point(-1, 0)
        self._move_right = Point(1, 0)
    
    def get_velocities(self):

        return (self._move_left, self._move_right)

    def execute(self, cast):
        
        position = cast["invaders"][0].get_position()

        x_position = position.get_x()
        max_x = constants.MAX_X
        
        if x_position <= 3:
            velocity = (self.get_velocities())[1]

            for invader in cast["invaders"]:
                invader.set_velocity(velocity)
       
        elif x_position >= (max_x - 30):
            velocity = (self.get_velocities())[0]

            for invader in cast["invaders"]:
                invader.set_velocity(velocity)

        
    