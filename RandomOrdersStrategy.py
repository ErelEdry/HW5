import random
from Customer import Customer
from Dish import Dish
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Explosive import Explosive
from Furious import Furious
from TypeA import TypeA
from TypeB import TypeB

class RandomOrdersStrategy:
    def __init__(self, max_dishes, max_ingredients, ingredients, n_orders=-1):
        if max_dishes < 1 or max_ingredients < 1:
            raise ValueError("max_dishes and max_ingredients must be at least 1")
        self.max_dishes = max_dishes
        self.max_ingredients = max_ingredients
        if isinstance(ingredients, dict):
            self.ingredients = list(ingredients.keys())
        else:
            self.ingredients = ingredients
        self.n_orders = n_orders
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n_orders != -1 and self.current >= self.n_orders:
            raise StopIteration
        self.current += 1
        num_ingredients = random.randint(1, self.max_ingredients)
        dish_ingredients = random.choices(self.ingredients, k=num_ingredients)
        dish = Dish(dish_ingredients)
        moods = [Chill(), Angry(), Calm(), Furious(), Explosive()]
        personalities = [TypeA(), TypeB()]
        mood = random.choice(moods)
        personality = random.choice(personalities)
        customer = Customer(name=self.current, mood=mood, personality=personality, initial_patience=100)
        return customer, dish