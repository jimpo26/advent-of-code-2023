with open('input.txt', 'r') as f:
    data = f.read()

# i completed the first part of the problem on my own, but i had to look up to a visual explanation for the second part
def part1(lines):
    groups = lines.split("\n\n")
    seeds = [int(x) for x in groups[0].replace("seeds: ", "").split(" ")]

    for group in groups[1:]:
        tmp = seeds.copy()
        for line in group.split("\n")[1:]:
            dest, src, offset = (int(x) for x in line.split(" "))
            for i in range(len(seeds)):
                if src <= seeds[i] < src + offset:
                    tmp[i] = tmp[i] - src + dest
        seeds = tmp.copy()
    print(min(seeds))


def part2(lines):
    groups = lines.split("\n\n")
    d = [int(x) for x in groups[0].replace("seeds: ", "").split(" ")]
    seeds = []
    for i in range(0, len(d), 2):
        seeds.append((d[i], d[i] + d[i + 1]))

    for group in groups[1:]:
        values = []
        for line in group.split("\n")[1:]:
            values.append([int(x) for x in line.split(" ")])
        new = []
        while len(seeds) > 0:
            seed_range = seeds.pop()
            for dest, src, offset in values:
                left = max(src, seed_range[0])
                right = min(src + offset, seed_range[1])
                if left < right:
                    new.append((left - src + dest, right - src + dest))
                    if left > seed_range[0]:
                        new.append((seed_range[0], left))
                    if right < seed_range[1]:
                        new.append((right, seed_range[1]))
                    break
            else:
                new.append(seed_range)
        seeds = new
    print(min(seeds)[0])

part1(data)
part2(data)