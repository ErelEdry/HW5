from Customer import Customer
from Dish import Dish
from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException

class FalafelStall:
    def __init__(self, strategy, ingredient_prices: dict[str, float | int], money: float, orders: dict[int, tuple[Customer, Dish]]):
        self.strategy = strategy
        self.ingredient_prices = ingredient_prices
        self.money = money
        self.orders = orders
        self.order_count = 0

    def order(self, customer: Customer, dish: Dish) -> int:
        for ingredient in dish.ingredients:
            if ingredient not in self.ingredient_prices:
                raise NoSuchIngredientException(ingredient)
        self.order_count += 1
        order_id = self.order_count
        self.orders[order_id] = (customer, dish)
        return order_id

    def get_next_order_id(self):
        if len(self.orders) == 0:
            raise OrderOutOfBoundsException()
        return self.strategy(self.orders)

    def serve_dish(self, order_id, dish):
        if order_id not in self.orders:
            raise NoSuchOrderException(order_id)
        if self.orders[order_id][1] != dish:  # Compare dishes
            raise NotCustomerDishException(dish, self.orders[order_id][1])
        self.money += self.calculate_cost(dish)
        del self.orders[order_id]

    def remove_order(self, order_id):
        if order_id not in self.orders:
            raise NoSuchOrderException(order_id)
        del self.orders[order_id]

    def calculate_cost(self, dish):
        cost = 0
        for ingredient in dish.ingredients:
            if ingredient not in self.ingredient_prices:
                raise NoSuchIngredientException(ingredient)
            cost += self.ingredient_prices[ingredient]
        return cost

    def get_orders(self):
        return self.orders

    def get_earning(self):
        return self.money