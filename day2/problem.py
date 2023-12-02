with open('input.txt', 'r') as f:
    data = f.readlines()


def part1(lines):
    counter = 0
    total = 0
    for line in lines:
        colors = {
            "b": 0,
            "r": 0,
            "g": 0
        }
        counter += 1
        find_num = False
        find_color = False
        possible = True
        cur = ""
        for i in range(len(line)):
            if line[i] == ";" or line[i] == "\n":
                if colors["b"] > 14 or colors["g"] > 13 or colors["r"] > 12:
                    possible = False
                    break
                colors["r"] = 0
                colors["g"] = 0
                colors["b"] = 0
                find_num = True
            if line[i] == ":" or line[i] == ",":
                find_num = True
            if find_num:
                if line[i].isnumeric():  # O(1) because it is only one char (equivalent to 48 <= ord(lines[i] <= 57)
                    cur += line[i]
                elif cur != '':
                    find_num = False
                    find_color = True
            if find_color and line[i].isalpha():
                colors[line[i]] += int(cur)
                cur = ''
                find_color = False
        if possible:
            total += counter
    print(total)


def part2(lines):
    counter = 0
    total = 0
    for line in lines:
        colors = {
            "b": 0,
            "r": 0,
            "g": 0
        }
        counter += 1
        find_num = False
        find_color = False
        cur = ""
        for i in range(len(line)):
            if line[i] == ":" or line[i] == "," or line[i] == ";":
                find_num = True
            if find_num:
                if line[i].isnumeric():  # O(1) because it is only one char (equivalent to 48 <= ord(lines[i] <= 57)
                    cur += line[i]
                elif cur != '':
                    find_num = False
                    find_color = True
            if find_color and line[i].isalpha():
                if colors[line[i]] < int(cur):
                    colors[line[i]] = int(cur)
                cur = ''
                find_color = False
        total += colors['r'] * colors['g'] * colors['b']
        print(total)

part2(data)