import time
from Angry import Angry
from Customer import Customer
from Dish import Dish
from FalafelStall import FalafelStall
from FixedOrdersStrategy import FixedOrdersStrategy
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from RandomOrdersStrategy import RandomOrdersStrategy
from TypeA import TypeA
from exceptions import NoSuchIngredientException, NotCustomerDishException, NoSuchOrderException


class Game:
    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.orders_strategy = orders_strategy
        self.serving_strategy = serving_strategy
        self.ingredient_prices = ingredient_prices
        self.lives = 3
        self.game_start = int(time.time())
        self.dictionary_ingredient = {i: ingredient for i, ingredient in enumerate(ingredient_prices.keys())}
        self.customer_counter = 0

    def get_lives(self):
        return self.lives

    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return current_time - self.game_start

    def run(self):
        stall = FalafelStall(self.serving_strategy, self.ingredient_prices, 0.0, {})
        orders_iterator = iter(self.orders_strategy)

        while self.lives > 0:
            try:
                customer, dish = next(orders_iterator)
                stall.order(customer, dish)
            except StopIteration:
                pass

            for order_id, (customer, _) in list(stall.get_orders().items()):
                customer.update()
                if customer.get_patience() <= 0:
                    print(f"Customer {customer.name} ran out of patience and left.")
                    stall.remove_order(order_id)
                    self.lives -= 1

            try:
                next_order_id = self.serving_strategy.select_next_order(stall.get_orders())
                customer, expected_dish = stall.get_orders()[next_order_id]

                print(f"\nCustomer:\n{customer}")
                print(f"Expected Dish: {expected_dish}")
                print("Insert ingredients:")
                for key, value in sorted(self.dictionary_ingredient.items(), key=lambda x: x[0]):
                    print(f"{key}: {value}")

                ingredients_input = input("Enter ingredient numbers separated by spaces: ").strip().split()
                suggested_ingredients = [self.dictionary_ingredient[int(i)] for i in ingredients_input if i.isdigit()]
                suggested_dish = Dish(suggested_ingredients)

                stall.serve_dish(next_order_id, suggested_dish)
                print(f"Order {next_order_id} served successfully!")
                stall.remove_order(next_order_id)

            except NotCustomerDishException as e:
                print(f"Failed to serve a Dish to customer\n{e}")
                print("Please try again. Make sure to follow the expected dish exactly.")
                self.lives -= 1

            except Exception as e:
                print(e)
                self.lives -= 1

            if not stall.get_orders() and self.lives <= 0:
                break

        print(f"Game Over. Total Earnings: {stall.get_earning()}")

s_s = LeastPatienceCustomerServingStrategy()
lst_orders = [
    [
        (Customer(0, Angry(), TypeA()), Dish(['french fries', 'humus', 'humus', 'humus']))
    ]
]

INGREDIENTS_PRICES = {
    'green salad': 3,
    'falafel': 5,
    'french fries': 4,
    'coleslaw': 2,
    'fried eggplants': 3,
    'tachina': 0,
    'humus': 1
}

fixed_strategy = FixedOrdersStrategy(lst_orders)
random_strategy = RandomOrdersStrategy(3, 5, INGREDIENTS_PRICES)
g1 = Game(random_strategy, s_s, INGREDIENTS_PRICES)
g1.run()