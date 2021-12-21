from collections import Counter, defaultdict
from itertools import chain, pairwise, product, permutations
from typing import Any, Dict, List, Tuple
import math

import read_input
from common import create_matrix, parse_coords, sign


def parse_input() -> List[Any]:
    lines = read_input.string()
    words = lines.split(' ')
    return int(words[-3][:-1]), int(words[-1][:-1])


def solve1(row, col) -> None:
    diagonal = row + col - 1
    top_left_triangle = diagonal * (diagonal - 1) // 2
    num = top_left_triangle + col
    code = 20151125
    for _ in range(1, num):
        code *= 252533
        code %= 33554393
    print(code)


def solve2(input) -> None:
    print(xxx)


if __name__ == '__main__':
    row, col = parse_input()
    print(row, col)
    # solve1(4, 1)
    solve1(row, col)
    # solve2(input)
