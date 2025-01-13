import unittest
from TypeA import TypeA
from Angry import Angry
from Explosive import Explosive
from Furious import Furious
from Calm import Calm

class TestTypeA(unittest.TestCase):
    def setUp(self):
        self.typeA = TypeA()
        self.calm = Calm()
        self.angry = Angry()
        self.furious = Furious()
        self.explosive = Explosive()

    def test_initial_mood(self):
        current_mood = self.calm
        new_mood = self.typeA.__adjust_mood(current_mood, 0)
        self.assertEqual(new_mood, current_mood)

    def test_angry_to_furious(self):
        current_mood = self.angry
        new_mood = self.typeA.__adjust_mood(current_mood, 31)
        self.assertIsInstance(new_mood, Furious)

    def test_furious_to_explosive(self):
        current_mood = self.furious
        new_mood = self.typeA.__adjust_mood(current_mood, 41)
        self.assertIsInstance(new_mood, Explosive)

    def test_no_mood_change_below_threshold(self):
        test_cases = [
            (self.calm, 19),
            (self.angry, 29),
            (self.furious, 39)
        ]
        for current_mood, waiting_time in test_cases:
            with self.subTest(mood=current_mood, time=waiting_time):
                new_mood = self.typeA.__adjust_mood(current_mood, waiting_time)
                self.assertEqual(new_mood, current_mood)

    def test_explosive_stays_explosive(self):
        current_mood = self.explosive
        new_mood = self.typeA.__adjust_mood(current_mood, 100)
        self.assertIsInstance(new_mood, Explosive)

    def test_repr(self):
        self.assertEqual(repr(self.typeA), "TypeA")

if __name__ == '__main__':
    unittest.main()