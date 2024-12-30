from Mood import Mood
class Chill(Mood):
    def __init__(self, strength:int =2, chill_modifier: float=0.5):
        self.strength = strength
        self.chill_modifier = chill_modifier

    def get_patience_factor(self, waiting_time: float) -> float:
        return round(1.1 * (waiting_time/5) * self.strength*self.chill_modifier, 2)

    def __repr__(self)-> str:
        return "Chill"