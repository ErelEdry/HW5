import unittest
from Dish import Dish

class TestDish(unittest.TestCase):

    def test_default_initialization(self):
        dish = Dish()
        self.assertEqual(dish.ingredients, [])

    def test_initialization_with_ingredients(self):
        ingredients = ["falafel", "hummus"]
        dish = Dish(ingredients)
        self.assertEqual(dish.ingredients, ingredients)

    def test_initialization_with_empty_ingredients(self):
        dish = Dish([])
        self.assertEqual(dish.ingredients, [])

    def test_add_ingredient_to_empty_dish(self):
        dish = Dish()
        dish.add_ingredient("falafel")
        self.assertIn("falafel", dish.ingredients)

    def test_add_ingredient_to_non_empty_dish(self):
        dish = Dish(["hummus"])
        dish.add_ingredient("falafel")
        self.assertIn("falafel", dish.ingredients)
        self.assertIn("hummus", dish.ingredients)

    def test_add_duplicate_ingredient(self):
        dish = Dish(["falafel"])
        dish.add_ingredient("falafel")
        self.assertEqual(dish.ingredients, ["falafel", "falafel"])

    def test_equality_with_same_ingredients(self):
        dish1 = Dish(["falafel", "hummus"])
        dish2 = Dish(["hummus", "falafel"])
        self.assertEqual(dish1, dish2)

    def test_equality_with_different_ingredients(self):
        dish1 = Dish(["falafel", "hummus"])
        dish2 = Dish(["falafel", "tahini"])
        self.assertNotEqual(dish1, dish2)

    def test_equality_with_different_lengths(self):
        dish1 = Dish(["falafel", "hummus"])
        dish2 = Dish(["falafel"])
        self.assertNotEqual(dish1, dish2)

    def test_equality_with_non_dish_object(self):
        dish = Dish(["falafel", "hummus"])
        self.assertNotEqual(dish, ["falafel", "hummus"])

    def test_repr_with_ingredients(self):
        dish = Dish(["falafel", "hummus"])
        self.assertEqual(repr(dish), "* falafel, hummus *")

    def test_repr_with_empty_ingredients(self):
        dish = Dish()
        self.assertEqual(repr(dish), "*  *")

    def test_repr_with_single_ingredient(self):
        dish = Dish(["falafel"])
        self.assertEqual(repr(dish), "* falafel *")

if __name__ == '__main__':
    unittest.main()