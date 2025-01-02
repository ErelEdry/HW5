import time
from Angry import Angry
from Customer import Customer
from Dish import Dish
from FalafelStall import FalafelStall
from FixedOrdersStrategy import FixedOrdersStrategy
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from RandomOrdersStrategy import RandomOrdersStrategy
from TypeA import TypeA
from exceptions import NoSuchIngredientException, NotCustomerDishException


class Game:
    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.orders_strategy = orders_strategy
        self.serving_strategy = serving_strategy
        self.ingredient_prices = ingredient_prices
        self.lives = 3
        self.game_start = int(time.time())
        self.dictionary_ingredient = {
            0: "green salad",
            1: "falafel",
            2: "french fries",
            3: "coleslaw",
            4: "fried eggplants",
            5: "tachina",
            6: "humus"
        }
        self.customer_counter = 0

    @staticmethod
    def check_for_input():
        import sys
        import msvcrt
        return msvcrt.kbhit()

    def get_lives(self):
        return self.lives

    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return current_time - self.game_start

    def run(self):
        stall = FalafelStall(self.serving_strategy, self.ingredient_prices, 0, {})
        while self.lives > 0:
            try:
                self.customer_counter += 1
                customer_name = self.customer_counter
                customer, dish = next(self.orders_strategy)
                customer.name = customer_name
                order_id = stall.order(customer, dish)
                while True:
                    print(f"Customer:\n{customer}")
                    print(f"Dish: {dish}")
                    print("Insert ingredients:")
                    for key, value in self.dictionary_ingredient.items():
                        print(f"{key}: {value}")

                    start_time = time.time()
                    while True:
                        current_time = time.time()
                        if current_time - start_time >= 1:
                            self.update_customers(stall)
                            start_time = current_time

                        if self.check_for_input():
                            break

                    ingredients_input = input().strip().split()
                    ingredients = [self.dictionary_ingredient.get(int(item), "") for item in ingredients_input]
                    try:
                        new_dish = Dish(ingredients)
                        stall.serve_dish(order_id, new_dish)
                        break
                    except NoSuchIngredientException as e:
                        print(f"Failed to create a Dish\n{e}\nplease retry.")
                    except NotCustomerDishException as e:
                        print(f"Failed to serve a Dish to customer\n{e}")
                        continue
                    except Exception as e:
                        print(f"An unexpected error occurred while serving the dish: {e}")
            except StopIteration:
                print("No more orders to process.")
                break
            except Exception as e:
                print(f"An unexpected error occurred while generating an order: {e}")
                continue

        print(f"Game Over\nscore: {stall.get_earning()}")

    def update_customers(self, stall):
        current_time = int(time.time())
        for order_id, (customer, dish) in list(stall.get_orders().items()):
            try:
                waiting_time = current_time - customer.arrive_time
                customer.update(waiting_time)
                if customer.get_patience() <= 0:
                    stall.remove_order(order_id)
                    self.lives -= 1
                    print(f"Customer {customer.name} left! Lives remaining: {self.lives}")
            except Exception as e:
                print(f"An unexpected error occurred while updating customer patience: {e}")


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