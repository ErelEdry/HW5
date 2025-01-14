import unittest
from unittest.mock import MagicMock, patch
from Calm import Calm


class TestCalm(unittest.TestCase):
    def setUp(self):
        self.calm = Calm()
        self.calm_strong = Calm(strength=5)

    def test_init(self):
        self.assertEqual(self.calm.__strength, 2)

    def test_custom_strength(self):
        self.assertEqual(self.calm_strong.__strength, 5)

    def test_get_patience_no_wait(self):
        factor = self.calm.get_patience_factor(0)
        self.assertEqual(factor, 2.0)

    def test_get_patience_factor_wait(self):
        factor = self.calm.get_patience_factor(10)
        expected = round((1.02 ** 2) * 2, 2)
        self.assertEqual(factor, expected)

    def test_get_patience_factor_different_strength(self):
        factor = self.calm_strong.get_patience_factor(10)
        expected = round((1.02 ** 2) * 5, 2)
        self.assertEqual(factor, expected)

    def test_repr(self):
        self.assertEqual(repr(self.calm), "Calm")

if __name__ == '__main__':
    unittest.main()