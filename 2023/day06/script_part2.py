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

round_time = ''
for time in rounds_times:
    round_time += str(time)
round_time = int(round_time)

round_distance = ''
for dist in rounds_distances:
    round_distance += str(dist)
round_distance = int(round_distance)

print(round_time)
print(round_distance)

outcomes = getOutcomes(round_time)

ways2win = []
ways2win.append(len(list(filter(
    lambda outcome: outcome['distance'] > round_distance, outcomes))))

# print(ways2win)

answer = math.prod(ways2win)

print(f'Answer: {answer}')
