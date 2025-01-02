from Dish import Dish

class NoSuchIngredientException(Exception):
    def __init__(self, ingredient: str):
        self.ingredient = ingredient

    def __str__(self):
        return f'Error:\n"{self.ingredient}" is an invalid ingredient.'


class NotCustomerDishException(Exception):
    def __init__(self, suggested_dish: Dish, expected_dish: Dish):
        self.suggested_dish = suggested_dish
        self.expected_dish = expected_dish

    def __str__(self):
        return f"Error:\nThe suggested dish:\t{self.suggested_dish}\nis not as expected:\t{self.expected_dish}."


class NoSuchOrderException(Exception):
    def __init__(self, order_id: int):
        self.order_id = order_id

    def __str__(self):
        return f'Error:\nOrderID: "{self.order_id}" does not exist.'


class OrderOutOfBoundsException(Exception):
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return "Error:\nNo orders are available to process."