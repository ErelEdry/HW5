import time

from Calm import Calm
from Chill import Chill
from Mood import Mood
from Personality import Personality


class Customer:
    def __init__(self, name: str, mood: Mood, personality: Personality, patience: float,initial_patience: float=100,arrive_time: int =0):
        self.name = name
        self.mood = mood
        self.personality = personality
        self.arrive_time = arrive_time if arrive_time else int(time.time())
        self.patience = self.patience
        self.initial_patience = initial_patience

    def get_mood(self)-> Mood:
        return self.mood

    def get_waiting_time(self, current_time: float=None)-> float:
        if current_time is None:
            current_time = int(time.time())
        return current_time - self.arrive_time

    def get_patience(self)-> float:
        return round(self.patience,2)

    def update(self, waiting_time=None):
        if waiting_time is None:
            waiting_time = int(time.time()) - self.arrive_time
            self.patience =  self.mood.get_patience_factor(waiting_time)
            self.mood = self.personality.adjust_mood(self.mood, self.initial_patience)

    def __repr__(self)-> str:
        max_line = max(len(self.name), len(str(self.mood)), len(str(self.personality)), len(str(self.patience)))
        star_line= "*"*(max_line+4)
        return (
            f"{star_line}\n"
            f"* name: {self.name.ljust(max_line)} *\n"
            f"* mood: {str(self.mood).ljust(max_line)} *\n"
            f"* personality: {str(self.personality).ljust(max_line)} *\n"
            f"* patience: {str(self.patience).ljust(max_line)} *\n"
            f"{star_line}"
        )


