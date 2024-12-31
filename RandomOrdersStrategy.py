import random

from Angry import Angry
from Calm import Calm
from Chill import Chill
from Explosive import Explosive
from Furious import Furious
from TypeA import TypeA
from TypeB import TypeB


class RandomOrdersStrategy:
    def __init__(self,current: int, max_dishes: int, ingredients: list[str],max_ingredients: int,n_orders: int=-1):
        self.current = current
        self.n_orders = n_orders
        self.max_dishes = max_dishes
        self.ingredients = ingredients
        self.max_ingredients = max_ingredients


def __iter__(self):
    return self
def __next__(self):
    moods=[Chill(),Angry(),Calm(),Furious(),Explosive()]
    personalities=[TypeA,TypeB]
    if self.n_orders == 0:
        raise StopIteration
    self.n_orders -= 1
    self.current += 1
    self.mood = random.choice(moods)
    self.personality = random.choice(personalities)
    self.name =self.current + 1
    return random.randint(0, self.max_dishes)

