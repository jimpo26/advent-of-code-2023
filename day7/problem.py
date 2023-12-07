from collections import Counter

with open('input.txt', 'r') as f:
    data = f.readlines()


def part1(lines):
    order = '23456789TJQKA'
    weights = {character: weight for weight, character in enumerate(order)}
    hands = []
    points = {
        "high": [],
        "one": [],
        "two": [],
        "three": [],
        "house": [],
        "four": [],
        "five": [],
    }
    hands_bid = {}
    for i in range(len(lines)):
        hand, bid = (x.replace("\n", "") for x in lines[i].split(' '))
        hands.append((hand, bid))
        hands_bid[hand] = bid
        pairs, three, four, five = 0, 0, 0, 0
        while len(hand) > 0:
            n = hand.count(hand[0])
            hand = hand.replace(hand[0], '')
            if n == 2:
                pairs += 1
            elif n == 3:
                three += 1
            elif n == 4:
                four += 1
            elif n == 5:
                five += 1
        if five == 0 and four == 0 and three == 0 and pairs == 0:
            points["high"].append(hands[i][0])
        elif five == 1:
            points["five"].append(hands[i][0])
        elif four == 1:
            points["four"].append(hands[i][0])
        elif three == 1 and pairs == 1:
            points["house"].append(hands[i][0])
        elif three == 1:
            points["three"].append(hands[i][0])
        elif pairs == 2:
            points["two"].append(hands[i][0])
        elif pairs == 1:
            points["one"].append(hands[i][0])
    idx = 1
    total = 0
    for k, v in points.items():
        if len(v) > 1:
            points[k] = sorted(v, key=lambda s: tuple(weights[char] for char in s))
        for i in range(len(points[k])):
            total += int(hands_bid[points[k][i]]) * idx
            idx += 1
    print(total)


def part2(lines):
    order = 'J23456789TQKA'
    weights = {character: weight for weight, character in enumerate(order)}
    hands = []
    points = {
        "high": [],
        "one": [],
        "two": [],
        "three": [],
        "house": [],
        "four": [],
        "five": [],
    }
    hands_bid = {}
    for i in range(len(lines)):
        hand, bid = (x.replace("\n", "") for x in lines[i].split(' '))
        hands.append((hand, bid))
        hands_bid[hand] = bid
        pairs, three, four, five = 0, 0, 0, 0
        counter = Counter(hand)
        if hand == "JJQ24":
            ...
        # if J in the counter
        if 'J' in counter:
            if counter.most_common(1)[0][0] == 'J':
                print(counter.most_common(2))
                try:
                    counter = Counter(hand.replace('J', counter.most_common(2)[1][0]))
                except IndexError:
                    counter = Counter(hand.replace('J', '2'))
            else:
                counter = Counter(hand.replace('J', counter.most_common(1)[0][0]))
        for k, v in counter.items():
            if v == 5:
                five += 1
            elif v == 4:
                four += 1
            elif v == 3:
                three += 1
            elif v == 2:
                pairs += 1
        if five == 0 and four == 0 and three == 0 and pairs == 0:
            points["high"].append(hands[i][0])
        elif five == 1:
            points["five"].append(hands[i][0])
        elif four == 1:
            points["four"].append(hands[i][0])
        elif three == 1 and pairs == 1:
            points["house"].append(hands[i][0])
        elif three == 1:
            points["three"].append(hands[i][0])
        elif pairs == 2:
            points["two"].append(hands[i][0])
        elif pairs == 1:
            points["one"].append(hands[i][0])
    idx = 1
    total = 0
    for k, v in points.items():
        if len(v) > 1:
            points[k] = sorted(v, key=lambda s: tuple(weights[char] for char in s))
        for i in range(len(points[k])):
            total += int(hands_bid[points[k][i]]) * idx
            idx += 1
    print(points)
    print(total)


part1(data)
part2(data)
