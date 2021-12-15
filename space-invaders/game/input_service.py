#
# Description:
#   The following class obtains the user input according to the keys pressed
#   by the user.
#
# OOP Principles Used:
#   Abstraction.
#   Encapsulation.
#
# Reasoning:
#   This class uses abstraction because it hides the complexity of the screen 
#   detecting user input behind the screen object.
#   It uses encapsulation by making the values of each key unaccessible for the user.

import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-2, 0) # a
        self._keys[100] = Point(2, 0) # d
        self._keys[112] = True
    

        
    def get_input(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        input = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            # Otherwise is going to return the boolena corresponding to
            # wether the ship needs to shoot or not.
            input = self._keys.get(event.key_code, Point(0, 0))

        return input



