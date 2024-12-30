from typing import Type

from Mood import Mood
from Explosive import Explosive
from Furious import Furious
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Personality import Personality

class TypeB(Personality):
    def adjust_mood(self, mood: Mood, waiting_time: float):
        if waiting_time > 120 and mood == Furious:
            return Explosive()
        elif waiting_time > 90 and mood == Angry:
            return Furious()
        elif waiting_time > 60 and mood == Calm:
            return Angry()
        elif waiting_time > 30 and mood == Chill:
            return Calm()

    def __repr__(self)-> str:
        return "TypeB"



