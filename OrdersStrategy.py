from abc import ABC, abstractmethod

class OrdersStrategy(ABC):
    @abstractmethod
    def order(self):
        pass