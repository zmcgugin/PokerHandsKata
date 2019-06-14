import unittest
from poker.poker_winner import find_winning_hand


class MyTest(unittest.TestCase):

    def test_high_card_1(self):
        zaks_hand = ('Zak', ['AS', '2H', '3H', 'JC', '8D'])
        jons_hand = ('Jon', ['KS', '2H', '3H', 'JC', '8D'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_high_card_2(self):
        zaks_hand = ('Zak', ['KS', '2H', '3H', 'JC', '8D'])
        jons_hand = ('Jon', ['6S', '2H', '3H', 'JC', 'AS'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_pair_beats_high_card(self):
        zaks_hand = ('Zak', ['KS', '2H', '3H', 'JC', 'KH'])
        jons_hand = ('Jon', ['6S', '2H', '3H', 'JC', 'AS'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_pair_beats_lower_pair(self):
        zaks_hand = ('Zak', ['QS', '2H', 'AH', 'JC', 'QH'])
        jons_hand = ('Jon', ['KS', 'KH', '3H', 'JC', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_two_pair_beats_pair(self):
        zaks_hand = ('Zak', ['QS', '2H', '7H', '2D', 'QH'])
        jons_hand = ('Jon', ['KS', 'KH', '3H', 'AC', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_two_pair_beats_lower_two_pair(self):
        zaks_hand = ('Zak', ['QS', 'QH', '7H', '4D', '4H'])
        jons_hand = ('Jon', ['KS', 'KH', '3H', '3C', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_three_of_a_kind_beats_two_pair(self):
        zaks_hand = ('Zak', ['QS', 'QH', '7H', '4D', '4H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_three_of_a_kind_beats_lower_three_of_a_kind(self):
        zaks_hand = ('Zak', ['QS', 'QH', 'QC', '2D', '4H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_straight_beats_three_of_a_kind(self):
        zaks_hand = ('Zak', ['6S', '7H', '8C', '9D', '10H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_straight_ace_can_be_used_as_low(self):
        zaks_hand = ('Zak', ['AS', '2H', '3C', '4D', '5H'])
        jons_hand = ('Jon', ['KS', 'KH', 'KC', '3C', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_straight_can_beat_lower_straight(self):
        zaks_hand = ('Zak', ['6S', '7H', '8C', '9D', '10H'])
        jons_hand = ('Jon', ['7S', '8H', '9C', '10C', 'JS'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_flush_can_beat_a_straight(self):
        zaks_hand = ('Zak', ['7S', '8H', '9C', '10C', 'JH'])
        jons_hand = ('Jon', ['5S', '9S', 'JS', '2S', 'AS'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_flush_can_beat_a_smaller_flush(self):
        zaks_hand = ('Zak', ['2H', '3H', '4H', '5H', 'AH'])
        jons_hand = ('Jon', ['5S', '9S', 'JS', '2S', 'KS'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_full_house_beats_flush(self):
        zaks_hand = ('Zak', ['2S', '3H', '4C', '5H', 'AH'])
        jons_hand = ('Jon', ['5S', '5S', '8S', '8S', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_full_house_beats_lower_full_house(self):
        zaks_hand = ('Zak', ['AS', 'AS', '7S', '7S', '7S'])
        jons_hand = ('Jon', ['5S', '5S', '8S', '8S', '8S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_four_of_a_kind_beats_full_house(self):
        zaks_hand = ('Zak', ['AS', 'AS', '7S', '7S', '7S'])
        jons_hand = ('Jon', ['5S', '2S', '2C', '2D', '2H'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_four_of_a_kind_beats_lower_four_of_a_kind(self):
        zaks_hand = ('Zak', ['AS', '8S', '8C', '8D', '8H'])
        jons_hand = ('Jon', ['5S', '2S', '2C', '2D', '2H'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_straight_flush_beats_quads(self):
        zaks_hand = ('Zak', ['AS', '8S', '8C', '8D', '8H'])
        jons_hand = ('Jon', ['5S', '6S', '7S', '8S', '9S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Jon')

    def test_straight_flush_beats_lower_straight_flush(self):
        zaks_hand = ('Zak', ['6S', '7S', '8S', '9S', '10S'])
        jons_hand = ('Jon', ['5S', '6S', '7S', '8S', '9S'])
        self.assertEqual(find_winning_hand([zaks_hand, jons_hand]), 'Zak')



