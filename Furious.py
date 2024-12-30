from Mood import Mood
class Furious(Mood):
    def __init__(self,strength: int=2):
        self.strength = strength

    def get_patience_factor(self, waiting_time: float) -> float:
        return (round(1.3 * (waiting_time/5) * self.strength, 2))*2

    def __repr__(self)-> str:
        return "Furious"
