with open('input.txt', 'r') as f:
    data = f.readlines()

# i can make this algorithm a lot better, but in this aoc i'm trying to use as less built in functions as possible
# so str.replace, str.split, str.find, etc are not allowed. isnumeric is allowed when checking only 1 char at a time
# because it takes O(1) time in this case
def part1(lines):
    total = 0
    card = 0
    for line in lines:
        winner = set()
        card = 0
        find_num, find_num_win = False, False
        complete_num = ''
        for c in line:
            if c == ":":
                find_num_win = True
            if c == "|":
                find_num_win = False
                find_num = True

            if find_num or find_num_win:
                if c.isnumeric():
                    complete_num += c
                elif complete_num != '':
                    if find_num:
                        if complete_num in winner:
                            card = 1 if card == 0 else card * 2
                    if find_num_win:
                        winner.add(complete_num)
                    complete_num = ''
        total += card
    print(total)


def part2(lines):
    total_cards = 0
    d_cards = {}
    idx = 0
    for line in lines:
        winner = set()
        win_count = 0
        find_num, find_num_win = False, False
        complete_num = ''
        idx += 1
        if idx not in d_cards:
            d_cards[idx] = 1
        for c in line:
            if c == ":":
                find_num_win = True
            if c == "|":
                find_num_win = False
                find_num = True

            if find_num or find_num_win:
                if c.isnumeric():
                    complete_num += c
                elif complete_num != '':
                    if find_num:
                        if complete_num in winner:
                            win_count += 1
                    if find_num_win:
                        winner.add(complete_num)
                    complete_num = ''
        for i in range(win_count):
            if idx+i+1 not in d_cards:
                d_cards[idx+i+1] = 1
            d_cards[idx+i+1] = d_cards[idx+i+1] + d_cards[idx]
        total_cards += d_cards[idx]
    print(d_cards)
    print(total_cards)


part2(data)
