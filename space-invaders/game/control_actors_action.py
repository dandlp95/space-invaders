from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        input = self._input_service.get_input()
        ship = cast["player_ship"][0]

        if isinstance(input, Point):
            
            ship.set_velocity(input)
        else:

            is_shooting = input
            ship.set_shooting(is_shooting)

            





