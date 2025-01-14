import unittest
from unittest.mock import Mock
from Customer import Customer
from Dish import Dish
from FalafelStall import FalafelStall
from exceptions import NoSuchIngredientException

class TestFalafelStall(unittest.TestCase):

    def setUp(self):
        self.strategy = Mock(return_value=1)
        self.ingredient_prices = {"falafel": 5.0, "hummus": 3.0, "tahini": 2.0}
        self.money = 100.0
        self.stall = FalafelStall(self.strategy, self.ingredient_prices, self.money, {})
        self.customer = Customer(name=1, mood=None, personality=None, initial_patience=100)
        self.dish = Dish(ingredients=["falafel", "hummus"])

    def test_order(self):
        order_id = self.stall.order(self.customer, self.dish)
        self.assertEqual(order_id, 1)
        self.assertEqual(len(self.stall.__orders), 1)
        self.assertEqual(self.stall.__orders[1], (self.customer, self.dish))

    def test_order_with_invalid_ingredient(self):
        invalid_dish = Dish(ingredients=["falafel", "invalid_ingredient"])
        with self.assertRaises(NoSuchIngredientException):
            self.stall.order(self.customer, invalid_dish)

    def test_order_count_increments(self):
        self.assertEqual(self.stall.__order_count, 0)
        self.stall.order(self.customer, self.dish)
        self.assertEqual(self.stall.__order_count, 1)
        self.stall.order(self.customer, self.dish)
        self.assertEqual(self.stall.__order_count, 2)

if __name__ == '__main__':
    unittest.main()