import unittest
import time
from unittest.mock import patch
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Mood import Mood
from Personality import Personality
from TypeA import TypeA
from Customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.calm_mood = Calm()
        self.angry_mood = Angry()
        self.typeA_personality = TypeA()
        self.customer = Customer(name=1, mood=self.calm_mood, personality=self.typeA_personality, initial_patience=100)

    def test_initialization(self):
        self.assertEqual(self.customer.name, 1)
        self.assertIsInstance(self.customer.mood, Calm)
        self.assertIsInstance(self.customer.personality, TypeA)
        self.assertEqual(self.customer.initial_patience, 100)
        self.assertEqual(self.customer.patience, 100)
        self.assertAlmostEqual(self.customer.arrive_time, time.time(), delta=1)

    def test_get_mood(self):
        self.assertEqual(self.customer.get_mood(), self.calm_mood)

    def test_get_waiting_time(self):
        with patch('time.time', return_value=time.time() + 10):
            waiting_time = self.customer.get_waiting_time()
            self.assertEqual(waiting_time, 10)

    def test_get_patience(self):
        self.customer.patience = 99.987
        self.assertEqual(self.customer.get_patience(), 99.99)

    def test_update_patience(self):
        with patch('time.time', return_value=time.time() + 5):
            self.customer.update()
            self.assertNotEqual(self.customer.patience, 100)
            self.assertIsInstance(self.customer.mood, Mood)

    def test_repr(self):
        expected_output = (
            "**********************\n"
            "* name: 1            *\n"
            "* mood: Calm         *\n"
            "* personality: TypeA *\n"
            "* patience: 100.0    *\n"
            "**********************"
        )
        self.assertEqual(repr(self.customer), expected_output)

if __name__ == '__main__':
    unittest.main()