import unittest
from FixedOrdersStrategy import FixedOrdersStrategy

class TestFixedOrdersStrategy(unittest.TestCase):

    def test_initialization(self):
        lst_orders = [1, 2, 3]
        strategy = FixedOrdersStrategy(lst_orders)
        self.assertEqual(strategy.lst_orders, lst_orders)
        self.assertEqual(strategy.__current_index, 0)

    def test_iteration(self):
        lst_orders = [1, 2, 3]
        strategy = FixedOrdersStrategy(lst_orders)
        results = []
        for order in strategy:
            results.append(order)
        self.assertEqual(results, [1, 2, 3])
        self.assertEqual(strategy.__current_index, 3)

    def test_next_order(self):
        lst_orders = [1, 2, 3]
        strategy = FixedOrdersStrategy(lst_orders)
        self.assertEqual(next(strategy), 1)
        self.assertEqual(next(strategy), 2)
        self.assertEqual(next(strategy), 3)
        self.assertEqual(strategy.__current_index, 3)

    def test_iteration_stop(self):
        lst_orders = [1, 2, 3]
        strategy = FixedOrdersStrategy(lst_orders)
        for _ in strategy:
            pass
        with self.assertRaises(StopIteration):
            next(strategy)

    def test_empty_list(self):
        lst_orders = []
        strategy = FixedOrdersStrategy(lst_orders)
        with self.assertRaises(StopIteration):
            next(strategy)

if __name__ == '__main__':
    unittest.main()