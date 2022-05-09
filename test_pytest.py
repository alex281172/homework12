import pytest
from barrel_generation import barrel_generation
from class_card_generation import Card

class TestCard:
    def test_card_generation(self):
        player = []
        player.append(1)
        player = Card()
        player.card_generation_class()
        assert len(player.new_card) == 27

    def test_answer1_player(self):
        Card.player_answer_class = lambda: 'y'
        answer = Card.player_answer_class()
        assert answer == 'y'

    def test_answer2_player(self):
        Card.player_answer_class = lambda: 'n'
        answer = Card.player_answer_class()
        assert answer == 'n'

    def test_answer_robot(self):
        Card.robot_answer_class = 'ваш выбор y - ДА | n - НЕТ -> '
        assert Card.robot_answer_class == 'ваш выбор y - ДА | n - НЕТ -> '

    def test_card_magic(self):
        card1 = Card()
        card2 = Card()
        card1.card_generation_class()
        card2.card_generation_class()
        assert len(card1) == len(card2)




def test_barrel():
    digit = barrel_generation()
    assert digit > 0 and digit <92

