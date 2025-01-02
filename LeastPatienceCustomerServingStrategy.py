from Customer import Customer
from Dish import Dish
from ServingStrategy import ServingStrategy
from exceptions import OrderOutOfBoundsException


class LeastPatienceCustomerServingStrategy(ServingStrategy):
    def select_next_order(self, orders: dict[int, tuple[Customer, Dish]]):
        if len(orders) == 0:
            raise OrderOutOfBoundsException()
        return min(orders.keys(), key=lambda k: orders[k][0].get_patience())