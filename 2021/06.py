from collections import Counter

import read_input


def solve_for_days(days):
    c = Counter(input)
    for i in range(days):
        old_c = c.copy()
        c = Counter()
        for timer, count in old_c.items():
            if timer == 0:
                c[6] += count
                c[8] += count
            else:
                c[timer - 1] += count
            # print(timer, count)

    print(sum(c.values()))


def solve1(input) -> None:
    solve_for_days(80)


def solve2(input) -> None:
    solve_for_days(256)


if __name__ == '__main__':
    input = read_input.numbers(single_line=True)
    # print(input)
    solve1(input)
    solve2(input)
