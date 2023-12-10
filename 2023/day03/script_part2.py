import re

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()

p_numbers = re.compile(r'[0-9]+')
p_gears = re.compile(r'\*')

numbers = []
gears = []

line_number = 1
for _line in data.splitlines():
    for match in p_numbers.finditer(_line):
        numbers.append(
            {
                'line': line_number,
                'number': eval(match.group()),
                # 'span': match.span(),
                'start': match.start(),
                'end': match.end(),
            })
    for match in p_gears.finditer(_line):
        gears.append(
            {
                'line': line_number,
                'symbol': match.group(),
                # 'span': match.span(),
                'start': match.start(),
                'end': match.end(),
            })
    line_number += 1

# print(numbers)
# print(gears)

# invert the search: end of number must be symbol start -1 or start of number must be symbol end +1 on the previous, same, or next line.
# then check if there are only 2 validators. if so, we have a valid gear.

ratios = []

for gear in gears:
    print(f'Processing at line {gear["line"]}, position {gear["start"]}...')
    parts_connected = list(filter(
        lambda num: (num['line'] - 1 <= gear['line'] <= num['line'] + 1) and (
            num['start'] - 1 <= gear['start']) and (gear['end'] <= num['end'] + 1), numbers))
    print(parts_connected)
    if len(parts_connected) == 2:
        ratios.append(parts_connected[0]['number']
                      * parts_connected[1]['number'])

print(ratios)

answer = sum(ratios)

print(f'Answer: {answer}')
