class Gamescore():
    """Keeps track of game score
    """
    def __init__(self):
        self._score = 0
        # self._enemies = enemies

    def get_score(self):
        return self._score

    def add_point(self, point):
        self._score += point


