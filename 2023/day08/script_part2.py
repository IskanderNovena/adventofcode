import re
import math

input_file = 'example_part2.txt'
# input_file = 'puzzle_input.txt'

debug = True
write_file = False

# Read the file
with open(input_file) as f:
    data = f.read()

instructions = data.splitlines()[0]

pattern = re.compile(r'(?P<node>.{3}) = \((?P<left>.{3}), (?P<right>.{3})\)')

maps = []

for item in data.splitlines()[2:]:
    maps.append({
        'node': pattern.match(item).group('node'),
        'L': pattern.match(item).group('left'),
        'R': pattern.match(item).group('right'),
    })

if debug:
    print(f'Instructions: {instructions}\n')


def getNextNode(current_node, way):
    return list(filter(lambda x: x['node'] == current_node[way], maps))[0]


# Get the number of steps required for each node, then use math.lcm() to find the total number of steps needed to be at the Z for all nodes at the same time

start_nodes = list(filter(lambda x: x['node'][-1] == 'A', maps))

step_array = list()
for node in start_nodes:
    print(f'Checking node:\n{node}')
    steps = 0
    idx = 0
    current_node = node
    arrived = False
    while arrived == False:
        steps += 1
        current_node = getNextNode(current_node, instructions[idx])
        if current_node['node'][-1] == 'Z':
            arrived = True
            step_array.append(steps)
            if debug:
                print(f'Steps for node {current_node["node"]}: {steps}')
        else:
            idx += 1
            if idx == len(instructions):
                idx = 0

if debug:
    print(f'Step array:\n{step_array}')

answer = math.lcm(*step_array)

print(f'Answer: {answer}')
