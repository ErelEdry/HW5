from Customer import Customer
from Dish import Dish
from ServingStrategy import ServingStrategy
from exceptions import OrderOutOfBoundsException


class LeastPatienceCustomerServingStrategy(ServingStrategy):
    def select_next_order(self, orders: dict[int, tuple[Customer, Dish]]):
        if len(orders) == 0:
            raise OrderOutOfBoundsException()

        ordered_orders_by_arrive_time = {
            k: v
            for k, v in sorted(
                orders.items(),
                key=lambda item: item[1][0].get_patience(),
            )
        }
        first_arrive_time_order = next(iter(ordered_orders_by_arrive_time))
        return first_arrive_time_order