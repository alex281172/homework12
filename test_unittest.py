import unittest

from class_card_generation import Card
from barrel_generation import barrel_generation

class TestCard(unittest.TestCase):

    def test_init(self):
        self.test_my = Card()
        self.assertEqual(self.test_my.digits, [])
        self.assertEqual(self.test_my.space_number, [])
        self.assertEqual(self.test_my.digits_for_card, [])
        self.assertEqual(self.test_my.answer, [])


    def test_card(self):
        player = []
        player.append(1)
        player = Card()
        player.card_generation_class()
        self.assertEqual(len(player.new_card),27)






