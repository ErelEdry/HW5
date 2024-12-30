from Mood import Mood


class Calm(Mood):
    def __init__(self,strength: int=1):
        self.strength = strength

    def get_patience_factor(self, waiting_time: float) -> float:
        return round(1.05 * (waiting_time/5) * self.strength, 2)

    def __repr__(self)-> str:
        return "Calm"