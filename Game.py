import time

from setuptools.command.build_ext import if_dl

from Dish import Dish
from FalafelStall import FalafelStall


class Game:
    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.orders_strategy = orders_strategy
        self.serving_strategy = serving_strategy
        self.ingredient_prices = ingredient_prices
        self.lives = 3
        self.game_start = int(time.time())
        self.dictionary_ingredient={
            0: "green salad",
            1: "falafel",
            2: "french fries",
            3: "coleslaw",
            4: "fried eggplants",
            5: "tachina",
            6: "humus"
        }

    def get_lives(self):
        return self.lives


    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return self.game_start - current_time

    def run(self):
        falafel_stall = FalafelStall(self.orders_strategy, self.ingredient_prices, 0, self.orders_strategy.get_orders())
        while self.lives > 0:
            try:
                order_id = falafel_stall.get_next_order_id()
                customer, dish = falafel_stall.get_orders()[order_id]
                cost = falafel_stall.calculate_cost(dish)
                falafel_stall.serve_dish(order_id, dish)
                print(f"Customer:\n{customer.__repr__()}\nDish: {dish.__repr__()}")
                print(f"Insert ingredients:\n{dish.ingredients}")

                dish_input = input()
                new_dish_ingredients = []
                for item in dish_input.split():
                    try:
                        number = int(item)
                        if 0 <= number <= 6:
                            new_dish_ingredients.append(self.dictionary_ingredient[number])
                        else:
                            new_dish_ingredients.append("")
                    except ValueError:
                        new_dish_ingredients.append("")

                new_dish = Dish(new_dish_ingredients)

                if new_dish != dish:
                    raise ValueError("Dish does not match the customer's order")

                falafel_stall.serve_dish(order_id, new_dish)
                print(f"Served dish: {new_dish.__repr__()}")

            except Exception as e:
                print(f"Failed to create a Dish\n{e}\nplease retry.")

            for order_id, (customer, _) in falafel_stall.get_orders().items():
                customer.update()
                if customer.get_patience() <= 0:
                    falafel_stall.remove_order(order_id)
                    self.lives -= 1

            if self.lives <= 0:
                print(f"Game Over\nscore: {falafel_stall.get_earning()}")
                break






