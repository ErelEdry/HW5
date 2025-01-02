import unittest
from unittest.mock import patch
from Customer import Customer
from Dish import Dish
from LongestWaitingTimeServingStrategy import LongestWaitingTimeServingStrategy
from exceptions import OrderOutOfBoundsException

class TestLongestWaitingTimeServingStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = LongestWaitingTimeServingStrategy()
        self.dish = Dish(ingredients=["Cheese", "Tomato"])
        self.customer1 = Customer(name=1, mood=None, personality=None, initial_patience=100)
        self.customer2 = Customer(name=2, mood=None, personality=None, initial_patience=100)
        self.customer3 = Customer(name=3, mood=None, personality=None, initial_patience=100)
        self.orders = {
            1: (self.customer1, self.dish),
            2: (self.customer2, self.dish),
            3: (self.customer3, self.dish),
        }

    @patch('time.time')
    def test_select_next_order(self, mock_time):
        mock_time.return_value = 100  # Simulate current time
        self.customer1.arrive_time = 90  # Waiting time = 10
        self.customer2.arrive_time = 80  # Waiting time = 20
        self.customer3.arrive_time = 95  # Waiting time = 5
        next_order = self.strategy.select_next_order(self.orders)
        self.assertEqual(next_order, 2)

    @patch('time.time')
    def test_select_next_order_equal_waiting_time(self, mock_time):
        mock_time.return_value = 100  # Simulate current time
        self.customer1.arrive_time = 90  # Waiting time = 10
        self.customer2.arrive_time = 90  # Waiting time = 10
        self.customer3.arrive_time = 90  # Waiting time = 10
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