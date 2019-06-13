import unittest
from poker.poker_winner import PokerWinner


class MyTest(unittest.TestCase):

    def test_high_card_1(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['AS', '2H', '3H', 'JC', '8D'])
        jons_hand = ('Jon', ['KS', '2H', '3H', 'JC', '8D'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Zak')

    def test_high_card_2(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['KS', '2H', '3H', 'JC', '8D'])
        jons_hand = ('Jon', ['6S', '2H', '3H', 'JC', 'AS'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Jon')

    def test_pair_beats_high_card(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['KS', '2H', '3H', 'JC', 'KH'])
        jons_hand = ('Jon', ['6S', '2H', '3H', 'JC', 'AS'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Zak')

    def test_pair_beats_lower_pair(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['QS', '2H', 'AH', 'JC', 'QH'])
        jons_hand = ('Jon', ['KS', 'KH', '3H', 'JC', '8S'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Jon')

    def test_two_pair_beats_pair(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['QS', '2H', '7H', '2D', 'QH'])
        jons_hand = ('Jon', ['KS', 'KH', '3H', 'AC', '8S'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Zak')

    def test_two_pair_beats_lower_two_pair(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['QS', 'QH', '7H', '4D', '4H'])
        jons_hand = ('Jon', ['KS', 'KH', '3H', '3C', '8S'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Jon')
