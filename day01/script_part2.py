import re

# input_file = 'example_part2.txt'
input_file = 'puzzle_input.txt'

replacements = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}

# Read the file
with open(input_file) as f:
    data = f.read()

# First extract every valid entry, even when overlapping
keys = (re.escape(k) for k in replacements.keys())
pattern = re.compile(r'(?=(' + '|'.join(keys) + r'))')

translated = ''
for _line in data.splitlines():
    translated += ' '.join(pattern.findall(_line)) + '\n'

# Now replace all valid entries with numbers
keys = (re.escape(k) for k in replacements.keys())
pattern = re.compile(r'(' + '|'.join(keys) + r')')
result = pattern.sub(lambda x: replacements[x.group()], translated)

answer = 0

for _line in result.splitlines():
    matches = re.findall('\\d{1}', _line)
    answer += int(f'{matches[0]}{matches[-1]}')

print(f'Answer: {answer}')
