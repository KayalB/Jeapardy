class Player:
    def __init__(self, name, color):
        self.name = name
        self.score = 0
        self.color = color
    def gets_tossup(self):
        self.score += 10
    def gets_bonus(self):
        self.score += 5
    def loses_tossup(self):
        if self.score > -20:
            self.score -= 10
    