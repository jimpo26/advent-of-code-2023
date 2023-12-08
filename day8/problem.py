import math

with open('input.txt', 'r') as f:
    data = f.read()


def part1(lines):
    direction, points = lines.split("\n\n")
    d = {}
    for line in points.split("\n"):
        key, value = line.split(" = (")
        d[key] = value[:-1].split(", ")
    cur = "AAA"
    idx = 0
    steps = 0
    while cur != "ZZZ":
        if idx >= len(direction):
            idx = 0
        if direction[idx] == "R":
            cur = d[cur][1]
        else:
            cur = d[cur][0]
        idx += 1
        steps += 1
    print(steps)

def part2(lines):
    direction, points = lines.split("\n\n")
    d = {}
    for line in points.split("\n"):
        key, value = line.split(" = (")
        d[key] = value[:-1].split(", ")
    idx = 0
    cur_nodes = []
    for k, v in d.items():
        if k[-1] == "A":
            cur_nodes.append(k)
    total = []
    for i in range(len(cur_nodes)):
        steps = 0
        while cur_nodes[i][-1] != "Z":
            if idx >= len(direction):
                idx = 0
            if direction[idx] == "R":
                cur_nodes[i] = d[cur_nodes[i]][1]
            else:
                cur_nodes[i] = d[cur_nodes[i]][0]
            idx += 1
            steps += 1
        total.append(steps)
    print(math.lcm(*total))


part1(data)
part2(data)
