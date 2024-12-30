from abc import ABC, abstractmethod
from Customer import Customer
from Dish import Dish


class ServingStrategy(ABC):
    @abstractmethod
    def select_next_order(self, orders: dict[int, tuple[Customer, Dish]]):
        pass