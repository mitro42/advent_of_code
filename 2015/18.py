from typing import List, Any
from itertools import chain

import read_input
from common import create_matrix


def parse_input() -> List[Any]:
    lines = read_input.strings()
    n = len(lines)
    m = []
    for l in lines:
        m.append([True if c == '#' else False for c in l])

    return m


neighbor_coords = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1],
                   [1, 0], [1, 1]]


def print_board(board):
    for l in board:
        print(''.join(['#' if v else '.' for v in l]))


def alive_now(m, row, col):
    n = len(m)
    if 0 <= row < n:
        if 0 <= col < n:
            return m[row][col]
    return False


def alive_next(m, row, col):
    live_neighbors = sum(
        [alive_now(m, row + r, col + c) for (r, c) in neighbor_coords])
    if alive_now(m, row, col):
        return live_neighbors in [2, 3]
    else:
        return live_neighbors == 3


def step(m, stuck):
    n = len(m)
    new_m = create_matrix(n, n, False)
    for row in range(n):
        for col in range(n):
            new_m[row][col] = alive_next(m, row, col)
    if stuck:
        new_m[0][0] = \
        new_m[n - 1][0] = \
        new_m[0][n - 1] = \
        new_m[n - 1][n - 1] = True
    return new_m


def solve(input, stuck) -> None:
    m = input
    for i in range(100):
        m = step(m, stuck)
        # print_board(m)
        # print()
    print(sum(chain(*m)))


if __name__ == '__main__':
    input = parse_input()
    # print_board(input)
    # print()
    solve(input, False)
    solve(input, True)
