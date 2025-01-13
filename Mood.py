from abc import ABC, abstractmethod

class Mood(ABC):
    @abstractmethod
    def __init__(self, strength=2):
        self.strength = strength
    @abstractmethod
    def __repr__(self):
        return self.__class__.__name__
    @abstractmethod
    def get_patience_factor(self, waiting_time):
        pass
