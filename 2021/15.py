import heapq
import math
from itertools import chain
from typing import List, Any

import read_input
from common import create_matrix


def parse_input() -> List[Any]:
    lines = read_input.strings()
    ret = []
    for l in lines:
        ret.append([int(c) for c in l])
    return ret


def print_board(board):
    for l in board:
        print(''.join([str(v) for v in l]))
    print()


def increase_map(m, n=1):
    nv = list(range(1, 10))
    nv = nv[n:] + nv[:n]
    return [[nv[v - 1] for v in row] for row in m]


def increase_row(row, n=1):
    nv = list(range(1, 10))
    nv = nv[n:] + nv[:n]
    return [nv[v - 1] for v in row]


def best_path(risk) -> None:
    neighbor_coords = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    rows = len(risk)
    cols = len(risk[0])

    best = create_matrix(rows, cols, math.inf)
    best[0][0] = 0
    q = []
    heapq.heappush(q, (0, (0, 0)))

    while q:
        crisk, cnode = heapq.heappop(q)

        if cnode == (rows - 1, cols - 1):
            print(crisk)
            return

        if best[cnode[0]][cnode[1]] < crisk:
            continue

        for cn in neighbor_coords:
            r = cnode[0] + cn[0]
            c = cnode[1] + cn[1]
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue

            new_risk = min(best[r][c], risk[r][c] + crisk)
            if new_risk < best[r][c]:
                best[r][c] = new_risk
                heapq.heappush(q, (new_risk, (r, c)))

    print(best[rows - 1][cols - 1])


def solve1(risk) -> None:
    best_path(risk)


def solve2(risk) -> None:
    big_row = [
        list(chain(*[increase_row(r, i) for i in range(5)])) for r in risk
    ]
    big = list(chain(*[increase_map(big_row, i) for i in range(5)]))
    best_path(big)


if __name__ == '__main__':
    input = parse_input()
    solve1(input)
    solve2(input)
