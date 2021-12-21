from itertools import product
from typing import Tuple
from functools import cache

import read_input


def parse_input():
    lines = read_input.strings(sep=' ')
    return int(lines[0][4]), int(lines[1][4])


def roll() -> int:
    num = 0
    while True:
        num %= 100
        num += 1
        yield num


def solve1(p1, p2) -> None:
    roll_count = 0
    p1_score = 0
    p2_score = 0
    r = roll()
    while True:
        step = next(r) + next(r) + next(r)
        roll_count += 3
        # total += step
        p1 = (p1 + step - 1) % 10 + 1
        p1_score += p1
        if p1_score >= 1000:
            break

        step = next(r) + next(r) + next(r)
        roll_count += 3
        # total += step
        p2 = (p2 + step - 1) % 10 + 1
        p2_score += p2

        if p2_score >= 1000:
            break
    print(min(p1_score, p2_score) * roll_count)


all_roll_sums = [sum(rolls) for rolls in product(range(1, 4), repeat=3)]


@cache
def solve2_rec(p1, p2, p1_score, p2_score, roll_sum, target,
               next_player) -> Tuple[int, int]:
    if next_player == 1:
        p1 = (p1 - 1 + roll_sum) % 10 + 1
        p1_score += p1
        if p1_score >= target:
            return 1, 0

        subs = [
            solve2_rec(p1, p2, p1_score, p2_score, s, target, 2)
            for s in all_roll_sums
        ]
    else:
        p2 = (p2 - 1 + roll_sum) % 10 + 1
        p2_score += p2
        if p2_score >= target:
            return 0, 1

        subs = [
            solve2_rec(p1, p2, p1_score, p2_score, s, target, 1)
            for s in all_roll_sums
        ]

    ret = sum([res[0] for res in subs]), sum([res[1] for res in subs])
    return ret


def solve2(p1, p2):
    subs = [solve2_rec(p1, p2, 0, 0, s, 21, 1) for s in all_roll_sums]
    print(max(sum([res[0] for res in subs]), sum([res[1] for res in subs])))


if __name__ == '__main__':
    p1, p2 = parse_input()
    # print(p1, p2)
    solve1(p1, p2)
    solve2(p1, p2)
