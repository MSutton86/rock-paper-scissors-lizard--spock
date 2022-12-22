from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        # display gestures
        
        for gesture in self.gestures:
            print(gesture)




        # prompt user for gesture, capture in variable

        # validate user input (save for last)