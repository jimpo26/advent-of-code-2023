with open('input.txt', 'r') as f:
    data = f.readlines()


def part1(lines):
    total = 0
    for line in lines:
        nums = line.split()
        numbers = []
        idx = 0
        numbers.append(nums)
        while True:
            new = []
            zeroes = 0
            for i in range(len(numbers[idx])-1, 0, -1):
                new.append(int(numbers[idx][i]) - int(numbers[idx][i-1]))
                if new[-1] == 0:
                    zeroes += 1
            numbers.append(list(reversed(new)))
            idx += 1
            if zeroes == len(new):
                break
        print(numbers)
        n = 0
        for i in range(len(numbers), 0, -1):
            n = n - int(numbers[i-1][0])
            print(n)
        total += n

    print(total)

def part2(lines):
    total = 0
    for line in lines:
        nums = line.split()
        numbers = []
        idx = 0
        numbers.append(nums)
        while True:
            new = []
            zeroes = 0
            for i in range(len(numbers[idx]) - 1, 0, -1):
                new.append(int(numbers[idx][i]) - int(numbers[idx][i - 1]))
                if new[-1] == 0:
                    zeroes += 1
            numbers.append(list(reversed(new)))
            idx += 1
            if zeroes == len(new):
                break
        print(numbers)
        n = 0
        for i in range(len(numbers), 0, -1):
            n = int(numbers[i - 1][0]) - n
            print(n)
        total += n
    print(total)


part1(data)
part2(data)
