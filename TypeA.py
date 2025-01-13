from Mood import Mood
from Explosive import Explosive
from Furious import Furious
from Angry import Angry
from Personality import Personality

class TypeA(Personality):
    def adjust_mood(self, mood, waiting_time):
        if waiting_time > 40:
            return Explosive(mood.strength)
        elif waiting_time > 30 and not isinstance(mood, Explosive):
            return Furious(mood.strength)
        elif waiting_time > 20 and not isinstance(mood, (Furious, Explosive)):
            return Angry(mood.strength)
        return mood

    def __repr__(self):
        return "TypeA"

