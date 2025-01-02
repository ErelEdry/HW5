from Mood import Mood


class Calm(Mood):
    def __init__(self, strength: int = 2):
        super().__init__(strength)

    def get_patience_factor(self, waiting_time):
        factor = round(1.02 ** (waiting_time / 5) * self.strength, 2)
        return factor

    def __repr__(self):
        return super().__repr__()

    def __eq__(self, other):
        return isinstance(other, Calm) and self.strength == other.strength