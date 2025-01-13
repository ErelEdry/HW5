import unittest
from Calm import Calm

class TestCalm(unittest.TestCase):
    def setUp(self):
        self.calm = Calm()
    def test_patience_factor(self):
        test_cases = [
            (0, 0.0),      
            (10, 2.1),     
            (15, 3.15),    
        ]
        for waiting_time, expected in test_cases:
            with self.subTest(waiting_time=waiting_time):
                result = self.calm.__get_patience_factor(waiting_time)
                self.assertEqual(result, expected)

    def test_repr(self):
        self.assertEqual(repr(self.calm), "Calm")

if __name__ == '__main__':
    unittest.main()