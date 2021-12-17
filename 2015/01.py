from itertools import accumulate

import read_input


def solve1(input: str) -> None:
    count = sum([1 if c == '(' else -1 for c in input])
    print(count)


def solve2(input: str) -> None:
    floors = list(accumulate([1 if c == '(' else -1 for c in input]))
    print(floors.index(-1) + 1)


if __name__ == '__main__':
    input = read_input.string()
    # print(input)
    solve1(input)
    solve2(input)
