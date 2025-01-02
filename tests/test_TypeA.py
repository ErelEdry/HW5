import unittest
from unittest.mock import Mock
from Mood import Mood
from Explosive import Explosive
from Furious import Furious
from Angry import Angry
from Calm import Calm
from Chill import Chill
from TypeB import TypeB

class TestTypeB(unittest.TestCase):

    def setUp(self):
        self.typeB = TypeB()

    def test_adjust_mood_explosive(self):
        mood = Mock(spec=Furious)
        adjusted_mood = self.typeB.adjust_mood(mood, 121)
        self.assertIsInstance(adjusted_mood, Explosive)

    def test_adjust_mood_furious(self):
        mood = Mock(spec=Angry)
        adjusted_mood = self.typeB.adjust_mood(mood, 91)
        self.assertIsInstance(adjusted_mood, Furious)

    def test_adjust_mood_angry(self):
        mood = Mock(spec=Calm)
        adjusted_mood = self.typeB.adjust_mood(mood, 61)
        self.assertIsInstance(adjusted_mood, Angry)

    def test_adjust_mood_calm(self):
        mood = Mock(spec=Chill)
        adjusted_mood = self.typeB.adjust_mood(mood, 31)
        self.assertIsInstance(adjusted_mood, Calm)

    def test_adjust_mood_no_change(self):
        mood = Mock(spec=Chill)
        adjusted_mood = self.typeB.adjust_mood(mood, 29)
        self.assertIsInstance(adjusted_mood, Mock)

    def test_adjust_mood_explosive_no_change(self):
        mood = Mock(spec=Explosive)
        adjusted_mood = self.typeB.adjust_mood(mood, 150)
        self.assertIsInstance(adjusted_mood, Mock)

    def test_adjust_mood_furious_no_change(self):
        mood = Mock(spec=Furious)
        adjusted_mood = self.typeB.adjust_mood(mood, 100)
        self.assertIsInstance(adjusted_mood, Mock)

    def test_adjust_mood_angry_no_change(self):
        mood = Mock(spec=Angry)
        adjusted_mood = self.typeB.adjust_mood(mood, 70)
        self.assertIsInstance(adjusted_mood, Mock)

    def test_adjust_mood_calm_no_change(self):
        mood = Mock(spec=Calm)
        adjusted_mood = self.typeB.adjust_mood(mood, 40)
        self.assertIsInstance(adjusted_mood, Mock)

    def test_adjust_mood_chill_no_change(self):
        mood = Mock(spec=Chill)
        adjusted_mood = self.typeB.adjust_mood(mood, 20)
        self.assertIsInstance(adjusted_mood, Mock)

if __name__ == '__main__':
    unittest.main()