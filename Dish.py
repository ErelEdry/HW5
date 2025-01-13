class Dish:
    def __init__(self, ingredients=None):
        self.ingredients = ingredients if ingredients is not None else []

    def __eq__(self, other):
            if not isinstance(other, Dish):
                return False
            return sorted(self.ingredients) == sorted(other.ingredients)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients

    def __repr__(self):
        ingredients_str = ", ".join(self.ingredients)
        return f"* {ingredients_str} *"