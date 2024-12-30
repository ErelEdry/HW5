from Mood import Mood
from Explosive import Explosive
from Furious import Furious
from Angry import Angry
from Personality import Personality
class TypeA(Personality):
    def adjust_mood(self, mood: Mood, waiting_time: float):
        if waiting_time > 40:
             return Explosive()
        if waiting_time > 30 and mood != Explosive:
             return  Furious()
        if waiting_time > 20 and (mood != Furious or mood != Explosive):
            return Angry()
    def __repr__(self)-> str:
        return "TypeA"



