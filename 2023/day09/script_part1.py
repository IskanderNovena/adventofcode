import re
import math

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

debug = False
write_file = False

# Read the file
with open(input_file) as f:
    data = f.read()


def getExtrapolation(differentials):
    if debug:
        print(f'getExtrapolation - differential: {differentials}')
    result = 0
    if debug:
        print([idx[-1] for idx in differentials if idx != []])
    result += sum([idx[-1] for idx in differentials if idx != []])
    return result


dataset = list()
for line in data.splitlines():
    differentials = [[int(x) for x in re.findall(r'\d+', line)]]
    if debug:
        print(f'Running for history:\n{differentials[0]}')
    y = 0
    while not all(v == 0 for v in differentials[y]):
        if debug:
            print(f'Current differentials: {differentials[y]}')
        differentials.append([differentials[y][idx] - differentials[y][idx - 1]
                             for idx in range(1, len(differentials[y]))])
        y += 1

    dataset.append({
        'history': differentials[0],
        'differentials': differentials[1:],
        'extrapolation': sum([idx[-1] for idx in differentials if idx != []]),
    })

if debug:
    print(dataset)

answer = sum(x['extrapolation'] for x in dataset)

print(f'Answer: {answer}')

histories = list()
for line in data.splitlines():
    histories.append([int(x) for x in re.findall(r'\d+', line)])

s = 0
for history in histories:
    # print(history)
    diffs = [[x for x in history]]
    y = 0
    while not all(v == 0 for v in diffs[y]):
        # print(diffs[y])
        diffs.append([diffs[y][x - 1] - diffs[y][x]
                     for x in range(1, len(diffs[y]))])
        y += 1

    s += sum([x[-1] for x in diffs if x != []])

print(f'Answer validation: {s}')

# 1866957968 too high
# 1725996962 too high
# 634555774 too low
