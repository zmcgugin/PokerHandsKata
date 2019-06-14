from poker.result import *
import functools

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
    'full_house': 7,
    'four_of_a_kind': 8,
    'straight_flush': 9
}

def find_winning_hand(hands):
    results = list(map(parse_hands, hands))
    return sorted(results, key=functools.cmp_to_key(sort))[0].hand[0]


def compare_tie_breaker(a, b, index=0):
    if a[index] == b[index]:
        return compare_tie_breaker(a, b, index + 1)
    else:
        return a[index] > b[index]


def parse_hands(hand):
    result = straight_flush(hand)
    if result is None:
        result = four_of_a_kind(hand)
    if result is None:
        result = full_house(hand)
    if result is None:
        result = flush(hand)
    if result is None:
        result = straight(hand)
    if result is None:
        result = three_of_a_kind(hand)
    if result is None:
        result = two_pair(hand)
    if result is None:
        result = pair(hand)
    if result is None:
        result = high_card(hand)
    return result


def high_card(hand):
    cards = get_cards_number_values(hand)
    tie_breaker = sorted(cards, reverse=True)
    return Result('high_card', hand, tie_breaker)


def pair(hand):
    hand_without_suits = get_cards_number_values(hand)
    pair = find_duplicates(hand_without_suits, 2)

    if pair:
        tie_breakers = create_tie_breaker_list(pair, hand_without_suits)
        return Result('pair', hand, tie_breakers)
    else:
        return None


def two_pair(hand):
    hand_without_suits = get_cards_number_values(hand)
    pairs = find_duplicates(hand_without_suits, 2)

    if pairs and len(pairs) == 2:
        tie_breakers = create_tie_breaker_list(pairs, hand_without_suits)
        return Result('two_pair', hand, tie_breakers)
    else:
        return None


def three_of_a_kind(hand):
    hand_without_suits = get_cards_number_values(hand)
    trips = find_duplicates(hand_without_suits, 3)

    if trips:
        tie_breakers = create_tie_breaker_list(trips, hand_without_suits)
        return Result('three_of_a_kind', hand, tie_breakers)
    else:
        return None


def straight(hand):
    hws = sorted(get_cards_number_values(hand))

    if is_straight(hws):
        # using number in middle of straight as a tie breaker to avoid low ace's
        return Result('straight', hand, [hws[2]])
    else:
        return None


def flush(hand):
    suits = sorted(get_cards_suits(hand))

    if is_flush(suits):
        return Result('flush', hand, sorted(get_cards_number_values(hand), reverse=True))
    else:
        return None


def full_house(hand):
    hand_without_suits = get_cards_number_values(hand)
    pair = find_duplicates(hand_without_suits, 2)
    trips = find_duplicates(hand_without_suits, 3)

    if pair and trips:
        return Result('full_house', hand, [trips[0], pair[0]])
    else:
        return None


def four_of_a_kind(hand):
    hand_without_suits = get_cards_number_values(hand)
    quads = find_duplicates(hand_without_suits, 4)

    if quads:
        tie_breakers = create_tie_breaker_list(quads, hand_without_suits)
        return Result('four_of_a_kind', hand, tie_breakers)
    else:
        return None


def straight_flush(hand):
    hws = sorted(get_cards_number_values(hand))
    suits = sorted(get_cards_suits(hand))

    if is_straight(hws) and is_flush(suits):
        # using number in middle of straight as a tie breaker to avoid low ace's
        return Result('straight_flush', hand, [hws[2]])
    else:
        return None


def create_tie_breaker_list(main_hand, full_hand):
    main_hand.sort(reverse=True)
    kickers = [x for x in full_hand if x not in main_hand]
    kickers.sort(reverse=True)
    main_hand.extend(kickers)
    return main_hand


def find_duplicates(numbers, number_of_dups):
    duplicateNumbers = []
    for x in card_values.values():
        duplicateCount = numbers.count(x)
        if duplicateCount == number_of_dups:
            duplicateNumbers.append(x)
    return duplicateNumbers


def get_cards_number_values(hand):
    return list(map(lambda x: card_values[x[:-1]], hand[1]))


def get_cards_suits(hand):
    return list(map(lambda x: x[len(x) - 1], hand[1]))


def is_straight(hws):
    low_ace_straight = hws[0] + 1 == hws[1] and hws[1] + 1 == hws[2] and hws[2] + 1 == hws[3] and hws[4] == 14
    straight = hws[0] + 1 == hws[1] and hws[1] + 1 == hws[2] and hws[2] + 1 == hws[3] and hws[3] + 1 == hws[4]
    return low_ace_straight or straight


def is_flush(suits):
    return suits.count(suits[0]) == 5


def sort(a, b):
    bigger_hand = hand_value[a.type] > hand_value[b.type]
    same_hand = hand_value[a.type] == hand_value[b.type]

    if same_hand:
        bigger_tie_breaker = compare_tie_breaker(a.tie_breaker, b.tie_breaker)
        if bigger_tie_breaker:
            return -1
        else:
            return 1

    if bigger_hand:
        return -1
    else:
        return 1
