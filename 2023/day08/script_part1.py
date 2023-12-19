import re
import math

# input_file = 'example_part1.txt'
# input_file = 'example_part1_2.txt'
input_file = 'puzzle_input.txt'

debug = False
write_file = False

# Read the file
with open(input_file) as f:
    data = f.read()

instructions = data.splitlines()[0]

pattern = re.compile(r'(?P<node>.{3}) = \((?P<left>.{3}), (?P<right>.{3})\)')

maps = []

for item in data.splitlines()[2:]:
    if debug:
        print(item)
    maps.append({
        'node': pattern.match(item).group('node'),
        'L': pattern.match(item).group('left'),
        'R': pattern.match(item).group('right'),
    })

if debug:
    print(f'Instructions: {instructions}\n')

steps = 0
idx = 0
current_node = 'AAA'
while idx < len(instructions):
    steps += 1
    current_node = list(filter(lambda x: x['node'] == current_node, maps))[
        0][instructions[idx]]
    if current_node == 'ZZZ':
        break
    idx += 1
    if idx == len(instructions):
        idx = 0

answer = steps

print(f'Answer: {answer}')
