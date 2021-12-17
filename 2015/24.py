import math
import operator
from functools import reduce
from itertools import combinations

import read_input


def group_weight(w, selected):
    return sum([w[i] for i in selected])


def generate_group(w, fraction):
    target_weight = sum(w) // fraction
    for max_count in range(1, len(w) + 1):
        for selected in combinations(w, max_count):
            gw = sum(selected)
            if gw == target_weight:
                yield selected


def solve1(input):
    smallest_group_size = math.inf
    min_entanglement = math.inf
    for g1 in generate_group(input, 3):
        g2g3 = input - set(g1)
        for g2 in generate_group(g2g3, 2):
            if smallest_group_size < len(g1):
                return min_entanglement
            entanglement = reduce(operator.mul, g1)
            min_entanglement = min(min_entanglement, entanglement)
            smallest_group_size = len(g1)
            # print(g1, g2, g3)
            break


def solve2(input) -> None:
    smallest_group_size = math.inf
    min_entanglement = math.inf
    for g1 in generate_group(input, 4):
        g2g3g4 = input - set(g1)
        for g2 in generate_group(g2g3g4, 3):
            g3g4 = g2g3g4 - set(g2)
            for g3 in generate_group(g3g4, 2):
                if smallest_group_size < len(g1):
                    return min_entanglement
                entanglement = reduce(operator.mul, g1)
                min_entanglement = min(min_entanglement, entanglement)
                smallest_group_size = len(g1)
                # print(g1, g2, g3, g3g4 - set(g3))
                break
            else:
                continue
            break


if __name__ == '__main__':
    input = set(read_input.numbers())
    # print(input)
    print(solve1(input))
    print(solve2(input))
