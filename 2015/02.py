from typing import List

import read_input


def parse_input() -> List[List[int]]:
    lines = read_input.strings()
    return [list(map(int, l.split('x'))) for l in lines]


def solve1(input: List[List[int]]) -> None:
    total = 0
    for g in input:
        g.sort()
        total += 3 * g[0] * g[1] + 2 * g[1] * g[2] + 2 * g[0] * g[2]
    print(total)


def solve2(input: List[List[int]]) -> None:
    total = 0
    for g in input:
        g.sort()
        total += 2 * (g[0] + g[1]) + g[0] * g[1] * g[2]
    print(total)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
