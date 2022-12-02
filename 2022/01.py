from typing import List

import sys


def solve1() -> None:
    max_sum = 0
    cur_sum = 0
    for line in sys.stdin:
        if line.strip():
            cur_sum += int(line.strip())
        else:
            max_sum = max(max_sum, cur_sum)
            cur_sum = 0

    print(max_sum)


def solve2() -> None:
    sums = []
    cur_sum = 0
    for line in sys.stdin:
        if line.strip():
            cur_sum += int(line.strip())
        else:
            sums.append(cur_sum)
            cur_sum = 0

    sums.append(cur_sum)

    print(sum(sorted(sums)[-3:]))


if __name__ == '__main__':
    # solve1()
    solve2()
