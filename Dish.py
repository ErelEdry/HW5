class Dish:
        def __init__(self,ingredients: list[str]=None):
            self.ingredients = ingredients

        def add_ingredient(self,ingredient):
            self.ingredients.append(ingredient)

        def __eq__(self,other: any)-> bool:
            if len(self.ingredients) != len(other.ingredients):
                return False

            for item1, item2 in zip(sorted(self.ingredients), sorted(other.ingredients)):
                if item1 != item2:
                    return False

            if type(self)!= Dish or type(other)!= Dish:
                return False
            return True

        def __repr__(self)-> str:
            ingredients_str = ", ".join(self.ingredients)
            return f"*{ingredients_str}*"
