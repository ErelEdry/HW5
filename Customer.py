import time
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Mood import Mood
from Personality import Personality
from TypeA import TypeA

class Customer:
    def __init__(self, name: int, mood: Mood, personality: Personality, initial_patience: float = 100, arrive_time: int = 0):
        self.name = name
        self.mood = mood
        self.personality = personality
        self.arrive_time = arrive_time if arrive_time else int(time.time())
        self.initial_patience = initial_patience
        self.patience = float(initial_patience)

    def get_mood(self) -> Mood:
        return self.mood

    def get_waiting_time(self, current_time: float = None) -> float:
        if current_time is None:
            current_time = int(time.time())
        return current_time - self.arrive_time

    def get_patience(self) -> float:
        return round(self.patience, 2)

    def update(self, waiting_time=None):
        if waiting_time is None:
            waiting_time = int(time.time()) - self.arrive_time
        patience_factor = self.mood.get_patience_factor(waiting_time)
        self.patience = round(max(0, self.initial_patience - patience_factor * waiting_time), 2)
        self.mood = self.personality.adjust_mood(self.mood, waiting_time)

    def __repr__(self) -> str:
        max_line = max(
            len("name: " + str(self.name.__repr__())),
            len("mood: " + str(self.mood.__repr__())),
            len("personality: " + str(self.personality.__repr__())),
            len("patience: " + str(self.patience.__repr__()))
        )
        star_line = "*" * (max_line + 4)
        return (
            f"{star_line}\n"
            f"* name: {str(self.name.__repr__()).ljust(max_line - len('name: '))} *\n"
            f"* mood: {str(self.mood.__repr__()).ljust(max_line - len('mood: '))} *\n"
            f"* personality: {str(self.personality.__repr__()).ljust(max_line - len('personality: '))} *\n"
            f"* patience: {str(self.patience.__repr__()).ljust(max_line - len('patience: '))} *\n"
            f"{star_line}"
        )
