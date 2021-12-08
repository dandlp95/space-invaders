from game.actor import Actor
from game.point import Point
# from game.weapon import Weapon

class Ship(Actor):
    """An Actor that can also shoot beams on command."""

    def __init__(self):
        super().__init__() # Will cause error?

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

    
