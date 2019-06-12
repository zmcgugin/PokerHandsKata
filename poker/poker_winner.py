


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

    def find_winning_hand(self, hands):
        winning_hand = PokerWinner.pair(hands)
        if winning_hand is None:
            winning_hand = PokerWinner.high_card(hands)
        return winning_hand[0]

    @staticmethod
    def high_card(hands):
        max_hand = None
        max_hand_value = 0
        for hand in hands:
            max_card_value = 0
            for card in hand[1]:
                current_card_value = PokerWinner.card_values[card[:-1]]
                if current_card_value > max_card_value:
                    max_card_value = current_card_value

            if max_card_value > max_hand_value:
                max_hand_value = max_card_value
                max_hand = hand

        return max_hand

    @staticmethod
    def pair(hands):
        highest_pair_hand = None
        highest_pair_value = 0
        for hand in hands:
            hand_without_suits = list(map(lambda val: val[:-1], hand[1]))
            maxCard = max(PokerWinner.find_duplicates(hand_without_suits, 2))
            if maxCard > highest_pair_value:
                highest_pair_value = maxCard
                highest_pair_hand = hand

        return highest_pair_hand

    @staticmethod
    def find_duplicates(numbers, numberOfDups):
        duplicateNumbers = [0]
        for x in PokerWinner.card_values.keys():
            duplicateCount = numbers.count(x)
            if duplicateCount == numberOfDups:
                duplicateNumbers.append(PokerWinner.card_values[x])
        return duplicateNumbers
