import re
import math

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

debug = False
write_file = True

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
    'J': 0,
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
    # J cards can pretend to be whatever card is best for the purpose of determining hand type;
    # for example, QJJQ2 is now considered four of a kind.
    # However, for the purpose of breaking ties between two hands of the same type, J is always treated as J,
    # not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.
    unique_cards_in_hand = list(set(hand))
    jokers_in_hand = hand.count('J')
    card_count = []
    for c in unique_cards_in_hand:
        card_count.append({
            'card': c,
            'cardvalue': card_values[c],
            'count': hand.count(c),
        })

    sorted_card_count = sorted(
        card_count, key=lambda k: (-k['count'], -k['cardvalue']))
    highest_regular_card = {'card': 'X', 'cardvalue': 0, 'count': 0} if jokers_in_hand == 5 else list(
        filter(lambda x: x['card'] != 'J', sorted_card_count))[0]
    if debug:
        print(highest_regular_card)
    highest_wildcard_count = sum(item['count'] for item in list(filter(
        lambda x: x['card'] == highest_regular_card['card'] or x['card'] == 'J', card_count)))

    if debug and hand == 'J222Q':
        print('---')
        print(highest_regular_card)
        print(sorted_card_count)
        print('---')
    match highest_wildcard_count:
        case 5:
            hand_type = hand_types['five-of-a-kind']
        case 4:
            hand_type = hand_types['four-of-a-kind']
        case 3:
            if len(list(filter(lambda x: x['card'] != highest_regular_card['card'] and x['card'] != 'J', card_count))) == 1:
                hand_type = hand_types['full-house']
            else:
                hand_type = hand_types['three-of-a-kind']
        case 2:
            if len(list(filter(lambda x: x['card'] != highest_regular_card['card'] and x['card'] != 'J', card_count))) == 2:
                hand_type = hand_types['two-pair']
            else:
                hand_type = hand_types['one-pair']
        case _:
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


hands = []

pattern = re.compile(r'(?P<hand>.{5})\s+(?P<bid>\d+)')

for item in data.splitlines():
    if debug:
        print(item)
    hands.append(getHand(pattern.search(item).group(
        'hand'), pattern.search(item).group('bid')))

rank = 1
answer = 0
hands_ranked = sorted(hands, key=lambda k: ((-k['hand-type']), -k['card-values']['0'], -k['card-values']
                      ['1'], -k['card-values']['2'], -k['card-values']['3'], -k['card-values']['4']), reverse=True)

for hand in hands_ranked:
    if debug:
        print(
            f'Hand: {hand["hand"]}, hand type: {hand["hand-type"]}, rank: {rank}')
    answer += (hand['bid'] * rank)
    rank += 1

if write_file:
    with open('test.txt', 'w') as test:
        for line in hands_ranked:
            test.write(f'{line}\n')

print(f'Answer: {answer}')
