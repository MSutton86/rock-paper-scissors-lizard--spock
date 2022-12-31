class Rules:

    def __init__(self, rock, scissors, paper, lizard, spock, gesture_1, gesture_2):
        self.rock = rock
        self.scissors = scissors
        self.paper = paper
        self.lizard = lizard
        self.spock = spock
        self.gesture_1 = gesture_1
        self.gesture_2 = gesture_2
        self.player_1_score = 0
        self.player_2_score = 0

    def decision_engine(self):
        if self.gesture_1 == self.gesture_2:
            print("It's a Tie!")
        elif self.gesture_1 == self.rock and self.gesture_2 == self.scissors or self.lizard:
            print("Player 1 wins!")
            self.player_1_score += 1
            return self.player_1_score
        elif self.gesture_1 == self.rock and self.gesture_2 == self.paper or self.spock:
            print("Player 2 wins!")
            self.player_2_score += 1
            return self.player_2_score
        elif self.gesture_1 == self.scissors and self.gesture_2 == self.paper or self.lizard:
            print("Player 1 wins!")
            self.player_1_score += 1
            return self.player_1_score
        elif self.gesture_1 == self.scissors and self.gesture_2 == self.spock or self.rock:
            print("Player 2 wins!")
            self.player_2_score += 1
            return self.player_2_score
        elif self.gesture_1 == self.paper and self.gesture_2 == self.rock or self.spock:
            print("Player 1 wins!")
            self.player_1_score += 1
            return self.player_1_score
        elif self.gesture_1 == self.paper and self.gesture_2 == self.lizard or self.scissors:
            print("Player 2 wins!")
            self.player_2_score += 1
            return self.player_2_score
        elif self.gesture_1 == self.lizard and self.gesture_2 == self.paper or self.spock:
            print("Player 1 wins!")
            self.player_1_score += 1
            return self.player_1_score
        elif self.gesture_1 == self.lizard and self.gesture_2 == self.scissors or self.rock:
            print("Player 2 wins!")
            self.player_2_score += 1
            return self.player_2_score
        elif self.gesture_1 == self.spock and self.gesture_2 == self.rock or self.scissors:
            print("Player 1 wins!")
            self.player_1_score += 1
            return self.player_1_score
        elif self.gesture_1 == self.spock and self.gesture_2 == self.lizard or self.paper:
            print("Player 2 wins!")
            self.player_2_score += 1
            return self.player_2_score

    
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