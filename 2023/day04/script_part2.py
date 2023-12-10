import re
# import math

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()

pattern = re.compile(r'Card\s+(?P<id>\d+):\s+(?P<wins>.*)\s+\|\s+(?P<card>.*)')
p_numbers = re.compile(r'\d+')

extra_scratchcards_won = []

cards = []
for _line in data.splitlines():
    matching_numbers = []
    # points = 0
    # print(_line)
    id = int(pattern.match(_line).group('id'))
    winning_numbers = [eval(i) for i in p_numbers.findall(
        pattern.match(_line).group('wins'))]
    card_numbers = [eval(i) for i in p_numbers.findall(
        pattern.match(_line).group('card'))]
    for num in winning_numbers:
        if num in card_numbers:
            matching_numbers.append(num)

    extra_to_process = extra_scratchcards_won.count(id)
    # print(f'Extra scratchcards to process: {extra_to_process}')
    # print(f'Extra scratchcards won: {len(matching_numbers)}')
    # print(f'Loops for matching numbers: {extra_to_process + 1}')
    x = 0
    while x < extra_to_process + 1:
        counter = 1
        # We don't have cards with a number higher than 220
        while counter <= len(matching_numbers) and id + counter <= 220:
            extra_scratchcards_won.append(id + counter)
            counter += 1
        x += 1

    # # For card-points: 2 to the power of (matches - 1)
    # if len(matching_numbers) >= 1:
    #     points = math.pow(2, len(matching_numbers) - 1)

    cards.append(
        {
            'id': id,
            'winning_numbers': winning_numbers,
            'card_numbers': card_numbers,
            'matching_numbers': matching_numbers,
            # 'points': points,
        }
    )

# print(extra_scratchcards_won)
answer = len(extra_scratchcards_won) + len(cards)

print(f'Answer: {answer}')
