from typing import List

import read_input


def solve1(depths: List[int]) -> None:
    count = sum([depths[i - 1] < depths[i] for i in range(1, len(depths))])
    print(count)


def calculate_moving_sums(l: List[int]) -> List[int]:
    return [sum(l[i:i + 3]) for i in range(0, len(l) - 2)]


def solve2(depths: List[int]) -> None:
    count = sum([depths[i - 1] < depths[i] for i in range(1, len(depths))])
    moving_sums = calculate_moving_sums(input)
    solve1(moving_sums)


if __name__ == '__main__':
    input = read_input.numbers()
    solve1(input)
    solve2(input)
