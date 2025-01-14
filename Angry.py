from Mood import Mood
class Angry(Mood):
    def __init__(self, strength=2):
        super().__init__(strength)

    def get_patience_factor(self, waiting_time):
        return round(( 1.3 ** (waiting_time/5)) * self.strength, 2)

    def __repr__(self):
        return super().__repr__()




