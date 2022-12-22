class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.gestures = ["rock", "scissors", "paper", "lizard", "spock"]
        self.score = 0
      

    # def game_choice(self, player):
    #     self.single_player = one_v_ai
    #     self.multi_player = one_v_one
    #     #will have to be imported 

    def choose_gesture(self):
        pass

    def score_point(self):
        self.score += 1









"rock" > "scissors"
"scissors" > "paper"
"paper" > "rock"
"rock" > "lizard"
"lizard" > "spock"
"spock" > "scissors"
"scissors" > "lizard"
"lizard" > "paper"
"paper" > "spock"
"spock" > "rock"