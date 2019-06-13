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
        'two_pair': 3
    }

    def find_winning_hand(self, hands):
        results = list(map(PokerWinner.parse_hands, hands))
        return sorted(results, key=functools.cmp_to_key(PokerWinner.sort))[0].hand[0]

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

    @staticmethod
    def compare_tie_breaker(a, b, index=0):
        if a[index] == b[index]:
            return PokerWinner.compare_tie_breaker(a, b, index + 1)
        else:
            return a[index] > b[index]

    @staticmethod
    def parse_hands(hand):
        result = PokerWinner.two_pair(hand)
        if result is None:
            result = PokerWinner.pair(hand)
        if result is None:
            result = PokerWinner.high_card(hand)
        return result

    @staticmethod
    def high_card(hand):
        cards = PokerWinner.get_cards(hand)
        tie_breaker = sorted(cards, reverse=True)
        tie_breaker.pop()
        return Result('high_card', hand, tie_breaker)

    @staticmethod
    def pair(hand):
        hand_without_suits = PokerWinner.get_cards(hand)
        pair = PokerWinner.find_duplicates(hand_without_suits, 2)

        if pair:
            pair.sort()
            tie_breakers = [x for x in hand_without_suits if x not in pair]
            tie_breakers.sort(reverse=True)
            pair.extend(tie_breakers)
            return Result('pair', hand, pair)
        else:
            return None

    @staticmethod
    def two_pair(hand):
        hand_without_suits = PokerWinner.get_cards(hand)
        pairs = PokerWinner.find_duplicates(hand_without_suits, 2)

        if pairs and len(pairs) == 2:
            pairs.sort(reverse=True)
            tie_breakers = [x for x in hand_without_suits if x not in pairs]
            tie_breakers.sort(reverse=True)
            pairs.extend(tie_breakers)
            return Result('two_pair', hand, pairs)
        else:
            return None

    @staticmethod
    def find_duplicates(numbers, number_of_dups):
        duplicateNumbers = []
        for x in PokerWinner.card_values.values():
            duplicateCount = numbers.count(x)
            if duplicateCount == number_of_dups:
                duplicateNumbers.append(x)
        return duplicateNumbers

    @staticmethod
    def get_cards(hand):
        return list(map(lambda x: PokerWinner.card_values[x[:-1]], hand[1]))
