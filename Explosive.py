from Mood import Mood
class Explosive(Mood):
    def __init__(self, strength: int = 2):
        super().__init__(strength)

    def get_patience_factor(self, waiting_time: float) -> float:
        return round(1.3 ** ((waiting_time * self.strength) / 5), 2)

    def __repr__(self):
        return super().__repr__()

    def __eq__(self, other):
        return isinstance(other, Explosive) and self.strength == other.strength