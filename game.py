import random
from rules import Rules

gestures = ["rock", "scissors", "paper", "lizard", "spock"]
player_input = input("Do you want to play Single Player or Multi Player? (Single or Multi)")
if player_input == "S" or "s" or "Single" or "single":
    player_1_input = input(f"Enter a Choice {gestures}") 
    print(player_1_input)
    player_2_input = random.choice(gestures)
    print(player_2_input)
    Rules.decision_engine(player_1_input, player_2_input)
elif player_input == "M" or "m" or "Multi" or "multi":
    player_1_input = input(f"Player 1, Enter a Choice {gestures}") 
    print(player_1_input)
    player_2_input = input(f"Player 2, Enter a Choice {gestures}") 
    print(player_2_input)
    Rules.decision_engine(player_1_input, player_2_input)
else:
    print("Please enter a valid choice ")
    player_input = input("Do you want to play Single Player or Multi Player? (Single or Multi)")