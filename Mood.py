from abc import ABC, abstractmethod

class Mood(ABC):
    def __init__(self, strength: int = 2):
        self.strength = strength
    def __repr__(self):
        return self.__class__.__name__
    @abstractmethod
    def get_patience_factor(self, waiting_time):
        pass
    def __eq__(self, other):
        pass