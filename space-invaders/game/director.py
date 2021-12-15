#
# Description:
#   The following class will direct the game by calling the execute method
#   for each object in the list.
#
# OOP Principles Used:
#   Abstraction
#   Polymorphism
#   Encapsulation
# Reasoning:
#   This class uses inheritance abstraction because it is hiding the game's complexity.
#   All that we can see is that an execute method is being called for each object in whatever
#   array we passed.
#   It uses polymorphism as the execute method means something different for each object in the 
#   array. 
#   It uses encapsulation as the cast and sript attributes that are passed, are not accessible
#   for the user. 
from time import sleep
from game import constants

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)