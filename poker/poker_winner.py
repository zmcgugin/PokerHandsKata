from poker.result import *
import functools


class PokerWinner:

    card_values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    hand_value = {
        'high_card': 1,
        'pair': 2,
        'two_pair': 3,
        'three_of_a_kind': 4,
        'straight': 5,
        'flush': 6,
        'full_house': 7
    }

    def find_winning_hand(self, hands):
        results = list(map(PokerWinner.parse_hands, hands))
        return sorted(results, key=functools.cmp_to_key(PokerWinner.sort))[0].hand[0]

    @staticmethod
    def compare_tie_breaker(a, b, index=0):
        if a[index] == b[index]:
            return PokerWinner.compare_tie_breaker(a, b, index + 1)
        else:
            return a[index] > b[index]

    @staticmethod
    def parse_hands(hand):
        result = PokerWinner.full_house(hand)
        if result is None:
            result = PokerWinner.flush(hand)
        if result is None:
            result = PokerWinner.straight(hand)
        if result is None:
            result = PokerWinner.three_of_a_kind(hand)
        if result is None:
            result = PokerWinner.two_pair(hand)
        if result is None:
            result = PokerWinner.pair(hand)
        if result is None:
            result = PokerWinner.high_card(hand)
        return result

    @staticmethod
    def high_card(hand):
        cards = PokerWinner.get_cards_number_values(hand)
        tie_breaker = sorted(cards, reverse=True)
        return Result('high_card', hand, tie_breaker)

    @staticmethod
    def pair(hand):
        hand_without_suits = PokerWinner.get_cards_number_values(hand)
        pair = PokerWinner.find_duplicates(hand_without_suits, 2)

        if pair:
            tie_breakers = PokerWinner.create_tie_breaker_list(pair, hand_without_suits)
            return Result('pair', hand, tie_breakers)
        else:
            return None

    @staticmethod
    def two_pair(hand):
        hand_without_suits = PokerWinner.get_cards_number_values(hand)
        pairs = PokerWinner.find_duplicates(hand_without_suits, 2)

        if pairs and len(pairs) == 2:
            tie_breakers = PokerWinner.create_tie_breaker_list(pairs, hand_without_suits)
            return Result('two_pair', hand, tie_breakers)
        else:
            return None

    @staticmethod
    def three_of_a_kind(hand):
        hand_without_suits = PokerWinner.get_cards_number_values(hand)
        trips = PokerWinner.find_duplicates(hand_without_suits, 3)

        if trips:
            tie_breakers = PokerWinner.create_tie_breaker_list(trips, hand_without_suits)
            return Result('three_of_a_kind', hand, tie_breakers)
        else:
            return None

    @staticmethod
    def straight(hand):
        hws = sorted(PokerWinner.get_cards_number_values(hand))
        low_ace_straight = hws[0] + 1 == hws[1] and hws[1] + 1 == hws[2] and hws[2] + 1 == hws[3] and hws[4] == 14
        straight = hws[0] + 1 == hws[1] and hws[1] + 1 == hws[2] and hws[2] + 1 == hws[3] and hws[3] + 1 == hws[4]

        if low_ace_straight or straight:
            # using number in middle of straight as a tie breaker to avoid low ace's
            return Result('straight', hand, [hws[2]])
        else:
            return None

    @staticmethod
    def flush(hand):
        suits = sorted(PokerWinner.get_cards_suits(hand))

        if suits.count(suits[0]) == 5:
            return Result('flush', hand, sorted(PokerWinner.get_cards_number_values(hand), reverse=True))
        else:
            return None

    @staticmethod
    def full_house(hand):
        hand_without_suits = PokerWinner.get_cards_number_values(hand)
        pair = PokerWinner.find_duplicates(hand_without_suits, 2)
        trips = PokerWinner.find_duplicates(hand_without_suits, 3)

        if pair and trips:
            return Result('full_house', hand, [trips[0], pair[0]])
        else:
            return None

    @staticmethod
    def create_tie_breaker_list(main_hand, full_hand):
        main_hand.sort(reverse=True)
        kickers = [x for x in full_hand if x not in main_hand]
        kickers.sort(reverse=True)
        main_hand.extend(kickers)
        return main_hand

    @staticmethod
    def find_duplicates(numbers, number_of_dups):
        duplicateNumbers = []
        for x in PokerWinner.card_values.values():
            duplicateCount = numbers.count(x)
            if duplicateCount == number_of_dups:
                duplicateNumbers.append(x)
        return duplicateNumbers

    @staticmethod
    def get_cards_number_values(hand):
        return list(map(lambda x: PokerWinner.card_values[x[:-1]], hand[1]))

    @staticmethod
    def get_cards_suits(hand):
        return list(map(lambda x: x[len(x) - 1], hand[1]))

    @staticmethod
    def sort(a, b):
        bigger_hand = PokerWinner.hand_value[a.type] > PokerWinner.hand_value[b.type]
        same_hand = PokerWinner.hand_value[a.type] == PokerWinner.hand_value[b.type]

        if same_hand:
            bigger_tie_breaker = PokerWinner.compare_tie_breaker(a.tie_breaker, b.tie_breaker)
            if bigger_tie_breaker:
                return -1
            else:
                return 1

        if bigger_hand:
            return -1
        else:
            return 1
