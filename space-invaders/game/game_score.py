class Gamescore():
    """Keeps track of game score
    """
    def __init__(self, enemies):
        self._score = 0
        self._enemies = enemies

    def get_score(self):
        return self._score

    def add_point(self, point):
        self._score += point
    
    def game_over(self):
        return "Game Over."

    def is_game_won(self):
        if self._score == self._enemies:
            return True
    

