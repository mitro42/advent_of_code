from itertools import pairwise
from collections import Counter

import read_input


def parse_input():
    lines = read_input.strings(sep=' ')
    template = lines[0][0]
    rules = {l[0]: l[2] for l in lines[2:]}

    return template, rules


def solve1(template, rules) -> None:
    pol = template
    for i in range(10):
        # print(i)
        new_pol = []
        for c1, c2 in pairwise(pol):
            if len(new_pol) == 0:
                new_pol.append(c1)
            if c1 + c2 in rules:
                new_pol.append(rules[c1 + c2])
            new_pol.append(c2)
        # print(new_pol)
        pol = new_pol

    cnt = Counter(pol)
    ordered_cnt = cnt.most_common()
    print(ordered_cnt[0][1] - ordered_cnt[-1][1])


def generate_level(template, rules, level):
    pol = template
    for i in range(level):
        # print(i)
        new_pol = []
        for c1, c2 in pairwise(pol):
            if len(new_pol) == 0:
                new_pol.append(c1)

            if len(rules[c1 + c2]) == 1:
                new_pol.append(rules[c1 + c2])
            else:
                new_pol.append(rules[c1 + c2][1:-1])

            new_pol.append(c2)
        # print(new_pol)
        pol = new_pol
    return ''.join(pol)


def solve2(template, rules) -> None:
    lrules = {}
    atoms = set(''.join(rules.keys()))
    lrules[5] = {}
    for a1 in atoms:
        for a2 in atoms:
            lrules[5][a1 + a2] = generate_level(a1 + a2, rules, 5)
            # print(a1, a2, len(lrules[5][a1 + a2]))

    lrules[10] = {}
    for a1 in atoms:
        for a2 in atoms:
            lrules[10][a1 + a2] = generate_level(lrules[5][a1 + a2], lrules[5],
                                                 1)
            # print(a1, a2, len(lrules[10][a1 + a2]))

    lrules[20] = {}
    for a1 in atoms:
        for a2 in atoms:
            lrules[20][a1 + a2] = generate_level(lrules[10][a1 + a2],
                                                 lrules[10], 1)
            # print(a1, a2, len(lrules[20][a1 + a2]))

    c20 = {k: Counter(v) for k, v in lrules[20].items()}
    cnt = Counter()
    for c1, c2 in pairwise(template):
        # print(c1, c2, cnt)
        for d1, d2 in pairwise(lrules[20][c1 + c2]):
            cnt[lrules[20][d1 + d2][0]] -= 1
            cnt += c20[d1 + d2]
    cnt[template[0]] += 1
    ordered_cnt = cnt.most_common()
    print(ordered_cnt[0][1] - ordered_cnt[-1][1])


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(*input)
    solve2(*input)
