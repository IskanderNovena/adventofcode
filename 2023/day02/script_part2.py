import re

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# # only 12 red cubes, 13 green cubes, and 14 blue cubes
# max_cubes_in_bag = {
#     'red': 12,
#     'green': 13,
#     'blue': 14
# }

# Read the file
with open(input_file) as f:
    data = f.read()

pattern = re.compile(r'Game (?P<id>\d+): (?P<sets>.*)')
p_blue = re.compile(r'(?P<blue>\d+) blue')
p_red = re.compile(r'(?P<red>\d+) red')
p_green = re.compile(r'(?P<green>\d+) green')

games = []
for _line in data.splitlines():
    games.append(
        {
            'id': int(pattern.match(_line).group('id')),
            'red': max([eval(i) for i in p_red.findall(
                pattern.match(_line).group('sets'))]),
            'green': max([eval(i) for i in p_green.findall(
                pattern.match(_line).group('sets'))]),
            'blue': max([eval(i) for i in p_blue.findall(
                pattern.match(_line).group('sets'))]),
            'power': max([eval(i) for i in p_red.findall(
                pattern.match(_line).group('sets'))]) *
            max([eval(i) for i in p_green.findall(
                pattern.match(_line).group('sets'))]) *
            max([eval(i) for i in p_blue.findall(
                pattern.match(_line).group('sets'))])
        }
    )

# matching_games = list(filter(
#     lambda set: set['red'] <= max_cubes_in_bag['red'] and set['blue'] <= max_cubes_in_bag['blue'] and set['green'] <= max_cubes_in_bag['green'], games))

# answer = sum(map(lambda x: x['id'], matching_games))
answer = sum(map(lambda x: x['power'], games))

print(f'Answer: {answer}')
