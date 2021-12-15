#
# Description:
#   The following class keeps track of the score of the user.
#
# OOP Principles Used:
#   Encapsulation.
#
# Reasoning:
#   This class uses encapsulation because the score cannot be accessed
#   directly by the user. It has to be accessed by using the appropriate method
#   get score. 

class Gamescore():
    """Keeps track of game score
    """
    def __init__(self):
        self._score = 0

    def get_score(self):
        return self._score

    def add_point(self, point):
        self._score += point


