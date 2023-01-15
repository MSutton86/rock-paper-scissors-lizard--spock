import random
from rules import rules
from decision_engine import Decision_Engine
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_1 = Human("Player_1")
        self.player_2 = AI("Player_2")

    def run_game(self):
        self.display_game_rules()
        self.select_game_type()
        self.run_round()
        self. display_winner()

    def display_game_rules(self):
        print(*rules, sep='\n')

    def select_game_type(self):
        response = input("How many human players (1-2)? ")
        if response == "2":
            self.player_2 = Human('Player 2')

    def run_round(self):
        round = 1
        while self.player_1.score < 2 and self.player_2.score < 2:
            print(f'ROUND{round}')
            self.display_scoreboard()
            self.choose_gestures()
            self.compare_gestures()
            round += 1

    def compare_gestures(self):
        if self.player_1.gesture == self.player_2.gesture:
            print("It's a tie! No points awarded")
        elif self.player_1.gesture == 'rock':
            if self.player_2.gesture == 'scissors' or self.player_2.gesture == 'lizard':
                self.player_1.score_point()
            else:
                self.player_2.score_point()
        elif self.player_1.gesture == 'scissors':
            if self.player_2.gesture == 'paper' or self.player_2.gesture == 'lizard':
                self.player_1.score_point()
            else:
                self.player_2.score_point()
        elif self.player_1.gesture == 'paper':
            if self.player_2.gesture == 'rock' or self.player_2.gesture == 'spock':
                self.player_1.score_point()
            else:
                self.player_2.score_point()
        elif self.player_1.gesture == 'lizard':
            if self.player_2.gesture == 'paper' or self.player_2.gesture == 'spock':
                self.player_1.score_point()
            else:
                self.player_2.score_point()
        elif self.player_1.gesture == 'spock':
            if self.player_2.gesture == 'scissors' or self.player_2.gesture == 'rock':
                self.player_1.score_point()
            else:
                self.player_2.score_point()

    def choose_gestures(self):
        self.player_1.choose_gesture()
        self.player_2.choose_gesture()

    def display_scoreboard(self):
        print(f'{self.player_1.name}: {self.player_1.score}')
        print(f'{self.player_2.name}: {self.player_2.score}')

    def display_winner(self):
        winner= None 
        if self.player_1.score >= 2:
            winner = self.player_1
        else:
            winner = self.player_2
        print(f'{winner.name} WINS THE GAME!!!')



# player_input = input("Do you want to play Single Player or Multi Player? (Single or Multi)")
# if player_input == "S" or "s" or "Single" or "single":
#     player_1_input = input(f"Enter a Choice {gestures}") 
#     print(player_1_input)
#     player_2_input = random.choice(gestures)
#     print(player_2_input)
#     Rules.decision_engine()
# elif player_input == "M" or "m" or "Multi" or "multi":
#     player_1_input = input(f"Player 1, Enter a Choice {gestures}") 
#     print(player_1_input)
#     player_2_input = input(f"Player 2, Enter a Choice {gestures}") 
#     print(player_2_input)
#     Rules.decision_engine(player_1_input, player_2_input)
# else:
#     print("Please enter a valid choice ")
#     player_input = input("Do you want to play Single Player or Multi Player? (Single or Multi)")
 