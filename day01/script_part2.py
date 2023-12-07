import re

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
}

# Read the file
with open("puzzle_input.txt") as f:
    data = f.read()

pattern = re.compile(
    r'(?s)(one|two|three|four|five|six|seven|eight|nine)', re.MULTILINE)
result = pattern.sub(lambda x: replacements[x.group()], data)

keys = (re.escape(k) for k in replacements.keys())
pattern = re.compile(r'(' + '|'.join(keys) + r')')
result = pattern.sub(lambda x: replacements[x.group()], data)

answer = 0
results = []

for _line in result.splitlines():
    matches = re.findall('\\d{1}', _line)
    # answer += int(f'{matches[0]}{matches[-1]}')
    results.append(int(f'{matches[0]}{matches[-1]}'))
    
for result in results:
    answer += result
    
print(f'Answer: {answer}')
