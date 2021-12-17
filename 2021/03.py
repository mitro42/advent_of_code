from typing import List

import read_input


def parse_input() -> List[List[int]]:
    lines = read_input.strings()
    ret = [list(map(int, list(l))) for l in lines]
    return ret


def common(input: List[List[int]]) -> List[int]:
    count = len(input)
    bits = len(input[0])
    ones = [0] * bits
    for l in input:
        for i, d in enumerate(l):
            ones[i] += d

    ret = []
    for i, d in enumerate(ones):
        ret.append(int(d >= count - d))
    return ret


def solve1(input: List[List[int]]) -> None:
    epsilon, gamma = 0, 0
    for d in common(input):
        if d:
            epsilon += 1
        else:
            gamma += 1
        epsilon *= 2
        gamma *= 2

    epsilon //= 2
    gamma //= 2
    print(gamma * epsilon)


def solve2(input: List[List[int]]) -> None:
    o2 = input[:]

    i = 0
    while len(o2) != 1:
        commons = common(o2)
        o2 = [v for v in o2 if v[i] == commons[i]]
        i += 1

    i = 0
    co2 = input[:]
    while len(co2) != 1:
        commons = common(co2)
        co2 = [v for v in co2 if v[i] != commons[i]]
        i += 1

    o2 = int(''.join(list(map(str, *o2))), 2)
    co2 = int(''.join(list(map(str, *co2))), 2)
    print(o2 * co2)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
