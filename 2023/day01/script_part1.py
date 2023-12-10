import re

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()

pattern = re.compile(
    r'\d{1}', re.MULTILINE)

answer = 0

for _line in data.splitlines():
    matches = pattern.findall(_line)
    answer += int(f'{matches[0]}{matches[-1]}')

print(f'Answer: {answer}')
