import unittest
from unittest.mock import patch, Mock
from RandomOrdersStrategy import RandomOrdersStrategy
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Explosive import Explosive
from Furious import Furious
from TypeA import TypeA
from TypeB import TypeB

class TestRandomOrdersStrategy(unittest.TestCase):

    def setUp(self):
        self.max_dishes = 5
        self.max_ingredients = 10
        self.ingredients = ["ing1", "ing2", "ing3"]
        self.n_orders = 3
        self.strategy = RandomOrdersStrategy(
            max_dishes=self.max_dishes,
            max_ingredients=self.max_ingredients,
            ingredients=self.ingredients,
            n_orders=self.n_orders
        )

    def test_initialization(self):
        self.assertEqual(self.strategy.__max_dishes, self.max_dishes)
        self.assertEqual(self.strategy.__max_ingredients, self.max_ingredients)
        self.assertEqual(self.strategy.__ingredients, self.ingredients)
        self.assertEqual(self.strategy.__n_orders, self.n_orders)

    @patch('random.choice')
    @patch('random.randint')
    def test_next_order(self, mock_randint, mock_choice):
        mock_randint.return_value = 3
        mock_choice.side_effect = [Chill(), TypeA]

        self.strategy.__current = 0
        result = self.strategy.__next__()

        self.assertEqual(result, 3)
        mock_randint.assert_called_once_with(0, self.max_dishes)
        self.assertEqual(mock_choice.call_count, 2)

    def test_iteration_stop(self):
        self.strategy.__n_orders = 0
        with self.assertRaises(StopIteration):
            self.strategy.__next__()

    def test_iteration(self):
        self.strategy.__n_orders = 2
        self.strategy.__current = 0

        with patch('random.choice') as mock_choice, patch('random.randint') as mock_randint:
            mock_randint.return_value = 2
            mock_choice.side_effect = [Angry(), TypeB, Calm(), TypeA]

            results = list(self.strategy)

            self.assertEqual(results, [2, 2])
            self.assertEqual(mock_randint.call_count, 2)
            self.assertEqual(mock_choice.call_count, 4)

if __name__ == '__main__':
    unittest.main()