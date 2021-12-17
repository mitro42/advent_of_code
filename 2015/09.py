import itertools
import math

import read_input


def parse_input():
    ret = {}
    lines = read_input.strings()
    for l in lines:
        parts = l.split(' ')
        ret[(parts[0], parts[2])] = int(parts[4])
        ret[(parts[2], parts[0])] = int(parts[4])
    return ret


def solve1(input):
    cities = set([k[0] for k in input])
    min_dist = math.inf
    for p in itertools.permutations(cities):
        # for i in range
        d = sum([input[p[i], p[i + 1]] for i in range(len(p) - 1)])
        min_dist = min(min_dist, d)

    print(min_dist)


def solve2(input):
    cities = set([k[0] for k in input])
    max_dist = 0
    for p in itertools.permutations(cities):
        # for i in range
        d = sum([input[p[i], p[i + 1]] for i in range(len(p) - 1)])
        max_dist = max(max_dist, d)

    print(max_dist)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
