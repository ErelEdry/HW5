import unittest
from Dish import Dish

class TestDish(unittest.TestCase):
    def setUp(self):
        self.empty_dish = Dish()
        self.dish_with_ingredients = Dish(['falafel', 'humus', 'tachina'])

    def test_init_empty(self):
        self.assertEqual(self.empty_dish.__ingredients, [])

    def test_init_with_ingredients(self):
        expected_ingredients = ['falafel', 'humus', 'tachina']
        self.assertEqual(self.dish_with_ingredients.__ingredients, expected_ingredients)

    def test_equality_same_ingredients(self):
        dish1 = Dish(['falafel', 'humus'])
        dish2 = Dish(['humus', 'falafel'])
        self.assertEqual(dish1, dish2)

    def test_equality_different_ingredients(self):
        dish1 = Dish(['falafel', 'humus'])
        dish2 = Dish(['falafel', 'coleslaw'])
        self.assertNotEqual(dish1, dish2)

    def test_equality_with_non_dish(self):
        dish = Dish(['falafel', 'humus'])
        non_dish = ['falafel', 'humus']
        self.assertNotEqual(dish, non_dish)

    def test_add_ingredient(self):
        self.empty_dish.add_ingredient('french fries')
        self.assertEqual(self.empty_dish.__ingredients, ['french fries'])

    def test_add_multiple_ingredients(self):
        dish = Dish()
        ingredients = ['green salad', 'fried eggplants', 'tachina']
        for ingredient in ingredients:
            dish.add_ingredient(ingredient)
        self.assertEqual(dish.__ingredients, ingredients)

    def test_get_ingredients(self):
        ingredients = self.dish_with_ingredients.get_ingredients()
        self.assertEqual(ingredients, ['falafel', 'humus', 'tachina'])

    def test_repr(self):
        dish = Dish(['falafel', 'humus'])
        self.assertEqual(str(dish), '* falafel, humus *')

    def test_repr_empty_dish(self):
        self.assertEqual(str(self.empty_dish), '*  *')


if __name__ == '__main__':
    unittest.main()