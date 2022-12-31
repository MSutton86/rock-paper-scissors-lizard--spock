import random
from player import Player

class AI(Player):

    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        for gesture in self.gestures:
            self.gestures = gesture(random)
            print(self.gestures)