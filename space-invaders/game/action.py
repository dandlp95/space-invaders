#
# Description:
#   The following class is a template for Objects that will need to do an Action (execute)
#   The Action will interact with actors and alter the game. 
#
# OOP Principles Used:
#   Polymorphism. 
#   
#
# Reasoning:
#   Polymorphism. Although polymorphism is not used specifically here, the Execute method will
#   behave a bit different, depending on the class inheriting from this class. 

class Action:
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")