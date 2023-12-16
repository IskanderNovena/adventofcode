import re
import math

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()

rounds_times = [eval(i) for i in re.findall(
    r'\d+', data.splitlines()[0], re.MULTILINE + re.DOTALL)]
rounds_distances = [eval(i) for i in re.findall(
    r'\d+', data.splitlines()[1], re.MULTILINE + re.DOTALL)]


def getOutcomes(round_time):
    outcomes = []
    to_calc = list(range(0, round_time + 1))
    for i in list(range(0, round_time + 1)):
        hold_button = i
        acceleration = hold_button * 1
        distance = (round_time - hold_button) * acceleration
        outcomes.append({
            'hold_button': hold_button,
            'acceleration': acceleration,
            'distance': distance,
        })
    return outcomes


# print(rounds_times)
# print(rounds_distances)


rounds = []

idx = 0
for round in rounds_times:
    rounds.append({
        'round': idx,
        'outcomes': getOutcomes(round)
    })
    idx += 1

# print(rounds)
# print(rounds[0])

idx = 0

ways2win = []
while idx < len(rounds):
    min_distance = rounds_distances[idx]
    ways2win.append(len(list(filter(
        lambda outcome: outcome['distance'] > min_distance, rounds[idx]['outcomes']))))
    idx += 1

# print(ways2win)

answer = math.prod(ways2win)

print(f'Answer: {answer}')
