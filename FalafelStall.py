from Customer import Customer
from Dish import Dish
from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, \
    NotCustomerDishException


class FalafelStall:
    def __init__(self, strategy, ingredient_prices: dict[str, float | int], money: float, orders: dict[int, tuple[Customer, Dish]]):
        self.strategy = strategy
        self.ingredient_prices = ingredient_prices
        self.money = money
        self.orders = orders

    def order(self, customer: Customer, dish: Dish):
        next_id = len(self.orders) + 1
        for ingredient in dish.ingredients:
            if ingredient not in self.ingredient_prices.values():
                raise NoSuchIngredientException(ingredient)
        self.orders[next_id] = (customer, dish)

    def get_next_order_id(self):
        if len(self.orders) == 0:
            raise OrderOutOfBoundsException()
        return self.strategy(self.orders)

    def serve_dish(self, order_id, dish):
        if order_id not in self.orders:
            raise NoSuchOrderException(order_id)
        if self.orders[order_id][1] != dish:
            raise NotCustomerDishException(order_id)
        self.money += dish.price
        del self.orders[order_id]

    def remove_order(self, order_id):
        if order_id not in self.orders:
            raise NoSuchOrderException(order_id)
        del self.orders[order_id]

    def calculate_cost(self, dish):
        for ingredient in dish.ingredients:
            if ingredient not in self.ingredient_prices.values():
                raise NoSuchIngredientException(ingredient)
        return sum(self.ingredient_prices[ingredient] for ingredient in dish.ingredients)

    def get_orders(self):
        return self.orders

    def get_earning(self):
        return self.money









