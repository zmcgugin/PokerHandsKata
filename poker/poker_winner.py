


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
        winning_hand = PokerWinner.pair(self, hands)
        if winning_hand is None:
            winning_hand = PokerWinner.high_card(self, hands)
        return winning_hand[0]

    def high_card(self, hands):
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

    def pair(self, hands):
        for hand in hands:
            hand_without_suits = list(map(lambda val: val[:-1], hand[1]))
            if len(set(hand_without_suits)) < len(hand_without_suits):
                return hand
        return None
