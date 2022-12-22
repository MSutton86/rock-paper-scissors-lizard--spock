class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["rock", "scissors", "paper", "Lizard", "Spock"]
        self.score = 0

    def choose_gesture(self):
        pass

    def score_points(self):
        self.score += 1


# def game_choice(self, player):
#     self.single_player = one_v_ai
#     self.multi_player = one_v_one

# "rock" > "scissors"
# "scissors" > "paper"
# "paper" > "rock"
# "rock" > "lizard"
# "lizard" > "spock"
# "spock" > "scissors"
# "scissors" > "lizard"
# "lizard" > "paper"
# "paper" > "spock"
# "spock" > "rock"

