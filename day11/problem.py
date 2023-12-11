from itertools import combinations
import math

with open('input.txt', 'r') as f:
    data = f.read().splitlines()


def part1(lines):
    l = lines.copy()
    #expand the universe
    idx_to_insert = 0
    for i in range(len(lines)):
        if lines[i].count('#') == 0:
            l.insert(idx_to_insert, '.'*len(l[i]))
            idx_to_insert += 1
        idx_to_insert += 1
    lines = l.copy()
    # loop by columns
    idx_to_insert = 0
    for col in zip(*lines):
        if col.count('#') == 0:
            for i in range(len(lines)):
                v = list(lines[i])
                v.insert(idx_to_insert, '.')
                lines[i] = ''.join(v)
            idx_to_insert += 1
        idx_to_insert += 1

    # substitute
    points = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                points.append((i,j))
    total = 0
    pairs = list(combinations(points, 2))

    # Print all pairs
    for pair in pairs:
        # calculate distance between points
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        x_dist = abs(x1 - x2)
        y_dist = abs(y1 - y2)
        total_dist = x_dist + y_dist
        total += total_dist
    print(total)


def part2(lines):
    # expand the universe
    memo = set()
    for i in range(len(lines)):
        if lines[i].count('#') == 0:
            lines[i] = '-'*len(lines[i])
            for j in range(len(lines[i])):
                memo.add((i, j))
    # loop by columns
    print(memo)
    idx_to_insert = 0
    for col in zip(*lines):
        if col.count('#') == 0:
            for i in range(len(lines)):
                v = list(lines[i])
                v[idx_to_insert] = '-'
                lines[i] = ''.join(v)
                memo.add((i, idx_to_insert))
        idx_to_insert += 1
    [print(line) for line in lines]
    # substitute
    print(memo)
    points = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                points.append((i, j))
    total = 0
    pairs = list(combinations(points, 2))

    # Print all pairs
    for pair in pairs:
        # calculate distance between points
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        x_dist = abs(x1 - x2)
        y_dist = abs(y1 - y2)
        a = x1 if x1 < x2 else x2
        b = x2 if x2 > x1 else x1
        millions = 0
        for i in range(a, b):
            if (i, y1) in memo:
                millions += 1
        c = y1 if y1 < y2 else y2
        d = y2 if y2 > y1 else y1
        for i in range(c, d):
            if (x1, i) in memo:
                millions += 1
        total_dist = x_dist + y_dist - millions
        total += (total_dist + millions * 1_000_000)


    print(total)


part1(data)
part2(data)
