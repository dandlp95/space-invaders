#
# Description:
#   The following class will get NPC Actors to automatically move from side to side, without
#   any user input required.
#
# OOP Principles Used:
#   Polymorphism
#   Encapsulation
#   Inheritance
#
# Reasoning:
#   This class uses Polymorphism because It is giving the Action's Execute method
#   a different behavior in order to get the Actors to move automatically from side
#   to side.
#   This class uses encapsulation because the velocities of the Actors are hidden
#   and are not accessible to the user.
#   It uses inheritance as it is inheriting the Action class in order to use the 
#   Execute template.



from game.ship import Ship
from game.point import Point
from game import constants
from game.action import Action
import random

class Ai(Action):
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

        
    