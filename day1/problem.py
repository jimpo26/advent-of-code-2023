import re

with open('input.txt', 'r') as f:
    data = f.readlines()


def part1(lines):
    total = 0
    for i in range(len(lines)):
        num_arr = [x for x in lines[i] if 48 <= ord(x) <= 57]
        if len(num_arr) > 0:
            total += int(num_arr[0] + num_arr[len(num_arr) - 1])
    print(total)


def part2(lines):
    letters_to_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for i in range(len(lines)):
        lines[i] = re.sub('(?=(one|two|three|four|five|six|seven|eight|nine))', lambda x: letters_to_num[x.group(1)],
                          lines[i])
    part1(lines)


part2(data)
