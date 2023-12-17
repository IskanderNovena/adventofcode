import re
import math

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()

card_values = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

hand_types = {
    'high-card': 1,
    'one-pair': 2,
    'two-pair': 3,
    'three-of-a-kind': 4,
    'full-house': 5,
    'four-of-a-kind': 6,
    'five-of-a-kind': 7,
}


def getHand(hand, bid):
    # Five of a kind, where all five cards have the same label: AAAAA
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # High card, where all cards' labels are distinct: 23456
    unique_cards_in_hand = list(set(hand))
    if len(unique_cards_in_hand) == 1:
        hand_type = hand_types['five-of-a-kind']
    elif len(unique_cards_in_hand) == 2:
        if list(filter(lambda x: hand.count(x) == 4, unique_cards_in_hand)):
            hand_type = hand_types['four-of-a-kind']
        else:
            hand_type = hand_types['full-house']
    elif len(unique_cards_in_hand) == 3:
        if len(list(filter(lambda x: hand.count(x) == 3, unique_cards_in_hand))) == 1:
            hand_type = hand_types['three-of-a-kind']
        else:
            hand_type = hand_types['two-pair']
    elif len(list(filter(lambda x: hand.count(x) == 2, unique_cards_in_hand))) == 1:
        hand_type = hand_types['one-pair']
    else:
        hand_type = hand_types['high-card']

    return {
        'hand-type': hand_type,
        'hand': hand,
        'card-values': {
            '0': card_values[hand[0]],
            '1': card_values[hand[1]],
            '2': card_values[hand[2]],
            '3': card_values[hand[3]],
            '4': card_values[hand[4]],
        },
        'bid': int(bid),
    }


# For sorting the resulting list of dicts: https://stackoverflow.com/a/62380576/19024815

hands = []

pattern = re.compile(r'(?P<hand>.{5})\s+(?P<bid>\d+)')

for item in data.splitlines():
    hands.append(getHand(pattern.search(item).group(
        'hand'), pattern.search(item).group('bid')))

# print('Hands:')
# for hand in hands:
#     print(hand)

rank = 1
answer = 0
hands_ranked = sorted(hands, key=lambda k: ((-k['hand-type']), -k['card-values']['0'], -k['card-values']
                      ['1'], -k['card-values']['2'], -k['card-values']['3'], -k['card-values']['4']), reverse=True)
# print('Hands ranked:')
for hand in hands_ranked:
    # print(f'Hand: {hand["hand"]}, rank: {rank}')
    answer += (hand['bid'] * rank)
    rank += 1

print(f'Answer: {answer}')
