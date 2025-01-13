import unittest
from Dish import Dish

class TestDish(unittest.TestCase):
    def setUp(self):
        self.empty_dish = Dish()
        self.simple_dish = Dish(["falafel"])
        self.complex_dish = Dish(["falafel", "humus"])

    def test_initialization(self):
        self.assertEqual(self.empty_dish.ingredients, [])
        self.assertEqual(self.simple_dish.ingredients, ["tachina"])
        self.assertEqual(self.complex_dish.ingredients, ["falafel", "humus","fried eggplants","french fries"])

    def test_eq(self):
        dish1 = Dish(["falafel", "fried eggplants"])
        dish2 = Dish(["fried eggplants", "falafel"])
        self.assertEqual(dish1, dish2)

        dish3 = Dish(["falafel", "tachina"])
        self.assertNotEqual(dish1, dish3)

        self.assertNotEqual(dish1, ["falafel", "humus"])

    def test_repr(self):
        self.assertEqual(repr(self.empty_dish), "*  *")
        self.assertEqual(repr(self.simple_dish), "* falafel *")
        self.assertEqual(repr(self.complex_dish), "* falafel, humus *")

    def test_get_ingredients(self):
        self.assertEqual(self.empty_dish.get_ingredients(), [])
        self.assertEqual(self.simple_dish.get_ingredients(), ["falafel"])
        self.assertEqual(self.complex_dish.get_ingredients(), ["falafel", "humus"])

if __name__ == '__main__':
    unittest.main()