from abc import ABC, abstractmethod

class OrdersStrategy(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __next__(self):
        pass