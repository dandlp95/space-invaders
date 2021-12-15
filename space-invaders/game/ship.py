#
# Description:
#   The following class represents an actor that can shoot a projectile(represented by a 2D movable
#    actor.)
#
# OOP Principles Used:
#   Inheritance.
#   Encapsulation.
#
# Reasoning:
#   This class uses inheritance because it inherits from the Actor class.
#   It uses encapsulation because the attributes can only be accessed through the methods designed for that.

from game.actor import Actor
from game.point import Point

class Ship(Actor):
    """An Actor that can also shoot beams on command."""

    def __init__(self):
        super().__init__() 

        self._shoot = False
        self._beam_direction = Point(0, 0)
    
    def set_shooting(self, is_shooting):
        self._shoot = is_shooting

    def is_shooting(self):
        return self._shoot
    
    def set_beam_velocity(self, beam_direction):
        self._beam_direction = beam_direction
    
    def get_beam_velocity(self):
        return self._beam_direction

    
