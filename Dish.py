class Dish:
    def __init__(self, ingredients: list[str] = None):
        self.ingredients = ingredients if ingredients is not None else []

        def __eq__(self, other):
            if not isinstance(other, Dish):
                return False
            return sorted(self.ingredients) == sorted(other.ingredients)

    def __repr__(self) -> str:
        ingredients_str = ", ".join(self.ingredients)
        return f"* {ingredients_str} *"