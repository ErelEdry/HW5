import unittest
from Customer import Customer
from Dish import Dish
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from exceptions import OrderOutOfBoundsException

class TestLeastPatienceCustomerServingStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = LeastPatienceCustomerServingStrategy()
        self.dish = Dish(ingredients=["Cheese", "Tomato"])
        self.customer1 = Customer(name=1, mood=None, personality=None, initial_patience=100)
        self.customer2 = Customer(name=2, mood=None, personality=None, initial_patience=100)
        self.customer3 = Customer(name=3, mood=None, personality=None, initial_patience=100)
        self.orders = {
            1: (self.customer1, self.dish),
            2: (self.customer2, self.dish),
            3: (self.customer3, self.dish),
        }

    def test_select_next_order(self):
        self.customer1.patience = 50
        self.customer2.patience = 30
        self.customer3.patience = 70
        next_order = self.strategy.select_next_order(self.orders)
        self.assertEqual(next_order, 2)

    def test_select_next_order_equal_patience(self):
        self.customer1.patience = 100
        self.customer2.patience = 100
        self.customer3.patience = 100
        next_order = self.strategy.select_next_order(self.orders)
        self.assertIn(next_order, [1, 2, 3])

    def test_select_next_order_empty(self):
        with self.assertRaises(OrderOutOfBoundsException):
            self.strategy.select_next_order({})

    def test_select_next_order_single(self):
        single_order = {1: (self.customer1, self.dish)}
        next_order = self.strategy.select_next_order(single_order)
        self.assertEqual(next_order, 1)

if __name__ == '__main__':
    unittest.main()