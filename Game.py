import time
from RandomOrdersStrategy import RandomOrdersStrategy
from Dish import Dish
from FalafelStall import FalafelStall
from exceptions import NotCustomerDishException, OrderOutOfBoundsException, NoSuchIngredientException


class Game:
    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.orders_strategy = orders_strategy
        self.serving_strategy = serving_strategy
        self.ingredient_prices = ingredient_prices
        self.lives = 3
        self.game_start = int(time.time())
        self.dictionary_ingredient = {i: ingredient for i, ingredient in enumerate(ingredient_prices.keys())}
        self.__customer_counter = 0
        self.money = 0

    def get_lives(self):
        return self.lives

    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return current_time - self.game_start

    def run(self):
        something = iter(self.orders_strategy)
        while self.lives > 0:
            stall = FalafelStall(self.serving_strategy, self.ingredient_prices)
            try:
                group = next(something)
                for customer, dish in group:
                    stall.order(customer, dish)

                while len(stall.get_orders()) > 0 and self.lives > 0:
                    try:
                        order_id = stall.get_next_order_id()
                        customer, expected_dish = stall.get_order(order_id)
                        while customer.get_patience() > 0:
                            curr_dish = "Dish: * " + ", ".join(expected_dish.get_ingredients()) + " *"
                            print(f"Customer:\n{customer}\n{curr_dish}")
                            print("Insert ingredients:")
                            for key, value in self.dictionary_ingredient.items():
                                print(f"{key}: {value}")

                            try:

                                input_ingredients = input()
                                input_indices = [int(index) for index in input_ingredients.split()]

                                player_ingredients = []
                                for index in input_indices:
                                    if index not in self.dictionary_ingredient:
                                        raise NoSuchIngredientException(f"Ingredient {index} does not exist.")
                                    player_ingredients.append(self.dictionary_ingredient[index])
                                player_dish = Dish(ingredients=player_ingredients)

                                if sorted(player_dish.get_ingredients()) != sorted(expected_dish.get_ingredients()):
                                    print(
                                        f"Failed to serve a Dish to customer\nError:\nThe suggested dish:\t* {', '.join(player_dish.get_ingredients())} *\nis not as expected:\t* {', '.join(expected_dish.get_ingredients())} *.")
                                    customer.update(waiting_time=customer.get_waiting_time())
                                    if customer.get_patience() <= 0:
                                        stall.remove_order(order_id)
                                        self.lives -= 1
                                        break
                                else:
                                    stall.serve_dish(order_id, player_dish)
                                    stall.remove_order(order_id)
                                    self.money += stall.get_earning()
                                    break

                            except (NoSuchIngredientException, ValueError) as e:
                                print(f"Error: {e}. Try again.")
                                customer.update(waiting_time=customer.get_waiting_time())
                                if customer.get_patience() <= 0:
                                    stall.remove_order(order_id)
                                    self.lives -= 1
                                    break

                    except OrderOutOfBoundsException:
                        print("Error: No orders are available to process.")
                        break

            except StopIteration:
                break

        print("Game Over")
        print(f"score: {self.money}")