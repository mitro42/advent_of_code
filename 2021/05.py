from typing import List, Any
from itertools import chain

from common import create_matrix, parse_coords, sign
import read_input


def parse_input() -> List[Any]:
    lines = read_input.strings(sep=' ')
    ret = []
    for l in lines:
        ret.append([parse_coords(l[0]), parse_coords(l[2])])
    return ret


def create_board(input):
    f = list(chain(*([*s, *e] for (s, e) in input)))
    n = max(f) + 1
    return create_matrix(n, n, 0)


def add1(board, tl: List[int], br: List[int]) -> None:
    if not (tl[0] == br[0] or tl[1] == br[1]):
        return

    x1 = min(tl[0], br[0])
    x2 = max(tl[0], br[0])
    y1 = min(tl[1], br[1])
    y2 = max(tl[1], br[1])

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            board[y][x] += 1


def add2(board, tl: List[int], br: List[int]) -> None:
    x1 = tl[0]
    x2 = br[0]
    y1 = tl[1]
    y2 = br[1]
    if x1 < x2:
        x2 += 1
    else:
        x2 -= 1

    if y1 < y2:
        y2 += 1
    else:
        y2 -= 1

    if not (tl[0] == br[0] or tl[1] == br[1]):
        for x, y in zip(range(x1, x2, sign(x2 - x1)),
                        range(y1, y2, sign(y2 - y1))):
            board[y][x] += 1

    else:
        x1 = min(tl[0], br[0])
        x2 = max(tl[0], br[0])
        y1 = min(tl[1], br[1])
        y2 = max(tl[1], br[1])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[y][x] += 1


def print_board(board):
    for l in board:
        print(''.join([str(v) if v > 0 else '.' for v in l]))


def solve1(input) -> None:
    board = create_board(input)
    for l in input:
        add1(board, *l)
        # print_board(board)
        # print()

    print(len([v for v in chain(*board) if v > 1]))


def solve2(input) -> None:
    board = create_board(input)
    for l in input:
        add2(board, *l)
        # print_board(board)
        # print()

    print(len([v for v in chain(*board) if v > 1]))


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
