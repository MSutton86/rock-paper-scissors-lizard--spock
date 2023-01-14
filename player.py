class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["rock", "scissors", "paper", "lizard", "spock"]
        self.gesture = ''
        self.score = 0

    def choose_gesture(self):
        pass

    def score_point(self):
        self.score += 1 
        print(f'{self.name} wins the round!')