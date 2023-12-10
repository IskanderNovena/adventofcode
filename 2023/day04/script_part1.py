import re
import math

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()

pattern = re.compile(r'Card\s+(?P<id>\d+):\s+(?P<wins>.*)\s+\|\s+(?P<card>.*)')
p_numbers = re.compile(r'\d+')

cards = []
for _line in data.splitlines():
    matching_numbers = []
    points = 0
    # print(_line)
    winning_numbers = [eval(i) for i in p_numbers.findall(
        pattern.match(_line).group('wins'))]
    card_numbers = [eval(i) for i in p_numbers.findall(
        pattern.match(_line).group('card'))]
    for num in winning_numbers:
        if num in card_numbers:
            matching_numbers.append(num)

    # print(len(matching_numbers))

    # For card-points: 2 to the power of (matches - 1)
    if len(matching_numbers) >= 1:
        points = math.pow(2, len(matching_numbers) - 1)

    cards.append(
        {
            'id': int(pattern.match(_line).group('id')),
            'winning_numbers': winning_numbers,
            'card_numbers': card_numbers,
            'matching_numbers': matching_numbers,
            'points': points,
        }
    )

# print(cards)

answer = int(sum(map(lambda x: x['points'], cards)))

print(f'Answer: {answer}')
