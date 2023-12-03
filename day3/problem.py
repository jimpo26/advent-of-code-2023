with open('input.txt', 'r') as f:
    data = f.readlines()


def part1(lines):
    total = 0
    for i in range(len(lines)):  # O(n)
        for k in range(len(lines[i])):  # O(m)
            if not lines[i][k].isnumeric() and lines[i][k] != "." and lines[i][k] != "\n":
                to_check = {"nw": (i-1, k-1), "n": (i-1, k), "ne": (i-1, k+1), "e": (i, k+1),
                            "se": (i+1, k+1), "s": (i+1, k), "sw": (i+1, k-1), "w": (i, k-1)}
                passed = set()
                for key in to_check:  # O(1)
                    if to_check[key] in passed:
                        continue
                    passed.add(to_check[key])
                    try:
                        if lines[to_check[key][0]][to_check[key][1]].isnumeric():
                            # left check
                            left, right = to_check[key][1], to_check[key][1]
                            while lines[to_check[key][0]][left].isnumeric():
                                left -= 1
                                passed.add((to_check[key][0], left))
                            while lines[to_check[key][0]][right].isnumeric():
                                right += 1
                                passed.add((to_check[key][0], right))
                            num = int(lines[to_check[key][0]][left+1:right])
                            print(num)
                            total += num
                    except IndexError:
                        pass
    print(total)


def part2(lines):
    total = 0
    for i in range(len(lines)):
        for k in range(len(lines[i])):
            if lines[i][k] == "*":
                to_check = {"nw": (i-1, k-1), "n": (i-1, k), "ne": (i-1, k+1), "e": (i, k+1),
                            "se": (i+1, k+1), "s": (i+1, k), "sw": (i+1, k-1), "w": (i, k-1)}
                passed = set()
                numbers = []
                for key in to_check:
                    if to_check[key] in passed:
                        continue
                    passed.add(to_check[key])
                    try:
                        if lines[to_check[key][0]][to_check[key][1]].isnumeric():
                            # left check
                            left, right = to_check[key][1], to_check[key][1]
                            while lines[to_check[key][0]][left].isnumeric():
                                left -= 1
                                passed.add((to_check[key][0], left))
                            while lines[to_check[key][0]][right].isnumeric():
                                right += 1
                                passed.add((to_check[key][0], right))
                            num = int(lines[to_check[key][0]][left+1:right])
                            numbers.append(num)
                    except IndexError:
                        pass
                if len(numbers) == 2:
                    total += numbers[0] * numbers[1]
    print(total)
    # overall complexity: O(n*m)
part2(data)

