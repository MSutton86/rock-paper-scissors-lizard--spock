from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def display_gestures(self):
        for num in range(len(self.gestures)):
            print(f'{num + 1}) {self.gestures[num]}')
     
    def choose_gesture(self):
        self.display_gestures()
        selection = int(input('Please choose a gesture (0-4): '))

        self.gesture = self.gestures[selection]
        print(f'{self.name} has chosen {self.gesture}')