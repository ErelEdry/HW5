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
        self.__max_dishes = max_dishes
        self.__max_ingredients = max_ingredients
        self.__group= 1
        self.__ingredients = ingredients
        self.__n_orders = n_orders
        self.__current = 0
        self.__conter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__n_orders != -1 and self.__current >= self.__n_orders:
            raise StopIteration

        group_list = []
        for _ in range(self.__group):
            if self.__n_orders != -1 and self.__current >= self.__n_orders:
                break
            name_id= self.__current + 1
            num_ingredients = random.randint(1, self.__max_ingredients)
            dish_ingredients = random.choices(self.__ingredients, k=num_ingredients)
            dish = Dish(ingredients=dish_ingredients)

            moods = [Chill(), Angry(), Calm(), Furious(), Explosive()]
            personalities = [TypeA(), TypeB()]

            mood = random.choice(moods)
            mood_name= mood
            personality = random.choice(personalities)
            personality_name=personality

            customer = Customer(name=name_id, mood= mood_name, personality=personality_name, initial_patience=100)
            group_list.append((customer, dish))
            self.__current += 1


        self.__conter+= self.__group

        return group_list
