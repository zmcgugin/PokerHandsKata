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

    def test_three_of_a_kind_beats_two_pair(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['QS', 'QH', '7H', '4D', '4H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Jon')

    def test_three_of_a_kind_beats_lower_three_of_a_kind(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['QS', 'QH', 'QC', '2D', '4H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Jon')

    def test_straight_beats_three_of_a_kind(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['6S', '7H', '8C', '9D', '10H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Zak')

    def test_straight_ace_can_be_used_as_low(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['AS', '2H', '3C', '4D', '5H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Zak')

    def test_straight_can_beat_lower_straight(self):
        subject = PokerWinner()
        zaks_hand = ('Zak', ['6S', '7H', '8C', '9D', '10H'])
        jons_hand = ('Jon', ['7S', '8H', '9C', '10C', 'JS'])
        self.assertEqual(PokerWinner.find_winning_hand(subject, [zaks_hand, jons_hand]), 'Jon')
