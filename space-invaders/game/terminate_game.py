#
# Description:
#   The following class is in charge of when and how to end the game.
#
# OOP Principles Used:
#   Polymorphism. 
#   Abstraction.
#   Encapsulation
#
# Reasoning:
#   This class uses polymorphism because it alters the Execute method to behave differently.
#   It uses abstraction because it hides the complexity of tracking the game score by working
#   with the game_score object and its methods.
#   It uses abstraction by making the game_score attribute unaccessible for the user.

import sys
from action import Action

class Terminate(Action):
    """Terminates game if player ship is destroyed or if player destroys all 
    invaders.
    """

    def __init__(self, game_score):
        
        self._game_score = game_score

    def get_score(self):

        return self._game_score.get_score()
    
    def display_score(self, message, score):

        print(message, "\n" + "Your score is: " + f"{score}")

    def execute(self, cast):
        
        # If the list that holds the players ship object is empty, game ends.
        if not cast["player_ship"]:
            message = "Game Over."
            self.display_score(message, self.get_score()) 

            sys.exit()

        elif not cast["invaders"]:
            message = "Congratulations. You Win."
            self.display_score(message, self.get_score())
            
            sys.exit()



    
    


