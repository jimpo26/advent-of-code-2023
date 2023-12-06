with open('input.txt', 'r') as f:
    data = f.read()

# When I saw this puzzle, my first reaction was: Ok, it seems pretty easy, but in the second half of the problem,
# there has to be a performance trap. And there was, so from the beginning I tried to perform as less iterations
# as possible, so instead of looping through all the possible values, I used the two pointers technique.
# I think that there also a better solution (maybe involving binary search?), but I'm pretty happy with this one.
def part1(lines):
    times, distances = lines.splitlines()
    times = times.split(':')[1].strip().split()
    distances = distances.split(':')[1].strip().split()
    total = 1
    num = 0
    for t, d in zip(times, distances):
        left, right = 1, int(t) - 1
        found = False
        while not found:
            traveled = (int(t) - left) * left
            if traveled > int(d):
                num = right - left + 1
                found = True
            else:
                left += 1
                right -= 1
        total *= num
    print(total)

def part2(lines):
    times, distances = lines.splitlines()
    time = "".join(times.split(':')[1].strip().split())
    dst = "".join(distances.split(':')[1].strip().split())
    total = 1
    num = 0
    left, right = 1, int(time) - 1
    found = False
    while not found:
        traveled = (int(time) - left) * left
        if traveled > int(dst):
            num = right - left + 1
            found = True
        else:
            left += 1
            right -= 1
    total *= num
    print(total)

part1(data)
part2(data)