from typing import List, Tuple

import read_input


def parse_input():
    lines = read_input.strings(sep=' ')
    ret = [(c, int(v)) for (c, v) in lines]
    return ret


def solve1(input: List[Tuple[str, int]]) -> None:
    horizontal = [l for l in input if l[0] == 'forward']
    vertical = [l for l in input if l[0] != 'forward']

    h = sum([v for (_, v) in horizontal])
    d = sum([v if c == 'down' else -v for (c, v) in vertical])
    print(h * d)


def solve2(input: List[Tuple[str, int]]) -> None:
    aim = 0
    pos = 0
    depth = 0
    for (c, v) in input:
        if c == 'forward':
            depth += aim * v
            pos += v
        elif c == 'down':
            aim += v
        elif c == 'up':
            aim -= v

    print(pos * depth)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
