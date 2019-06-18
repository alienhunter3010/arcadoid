class Stats:
    def __init__(self, lifes=3, score=0):
        self.score = score
        self.lifes = lifes

    def addScore(self, score):
        self.score += score
        return self.score

    def scaleLifes(self, life=-1):
        self.lifes += life
        return self.lifes