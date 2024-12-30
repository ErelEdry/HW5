from abc import ABC, abstractmethod

class Mood(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def get_patience_factor(self, waiting_time):
        pass
    def __repr__(self):
        pass