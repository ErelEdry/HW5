import unittest
from Calm import Calm

class TestCalm(unittest.TestCase):
    def setUp(self):
        self.calm = Calm()

    def test_get_patience_factor(self):
        self.assertEqual(self.calm.get_patience_factor(10), 2.1)
        self.assertEqual(self.calm.get_patience_factor(5), 1.05)
        self.assertEqual(self.calm.get_patience_factor(0), 0.0)
        self.assertEqual(self.calm.get_patience_factor(15), 3.15)
        self.assertEqual(self.calm.get_patience_factor(20), 4.2)
        self.assertEqual(self.calm.get_patience_factor(25), 5.25)


    def test___repr__(self):
        self.assertEqual(self.calm.__repr__(), "Calm")



