import re

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()

p_numbers = re.compile(r'[0-9]+')
p_symbols = re.compile(r'[^\.0-9]')

numbers = []
symbols = []

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
    for match in p_symbols.finditer(_line):
        symbols.append(
            {
                'line': line_number,
                'symbol': match.group(),
                # 'span': match.span(),
                'start': match.start(),
                'end': match.end(),
            })
    line_number += 1

# print(numbers)
# print(symbols)

part_numbers = []

for part in numbers:
    print(f'Processing {part["number"]}...')
    if list(filter(
        lambda sym: (part['line'] - 1 <= sym['line'] <= part['line'] + 1) and (
            part['start'] - 1 <= sym['start']) and (sym['end'] <= part['end'] + 1), symbols)):
        part_numbers.append(part)

print(part_numbers)

answer = sum(map(lambda x: x['number'], part_numbers))

print(f'Answer: {answer}')
