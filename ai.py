import random
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        self.gesture=random.choice(self.gestures)
        print(f'{self.name} has chosen {self.gesture}')