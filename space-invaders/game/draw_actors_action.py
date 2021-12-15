#
# Description:
#   Uses the output service to draw the Actors on the screen, according to its text, speed and 
#   position attributes.
#
# OOP Principles Used:
#   Inheritance.
#   Abstraction.
#   Polymorphism. 
#   Encapsulation
#
# Reasoning:
#   This class uses inheritance because it is inheriting from the Action class.
#   It uses abstraction because the complexity of drawing an object on the screen is hidden with a
#   simple for loop in the execute method that is simply calling each Actor in the array and putting
#   it in the ouput_service class which is the class that actually handles all the complexity.
#   It uses polymorphism because the it changes the behavior of the execute method that was inherited from the
#   Action class.
#   It uses encapsulation because it hides the output_service attribute from the user and can't be accessed directly
#   by the user.
from game.action import Action


class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)

            
        self._output_service.flush_buffer()
