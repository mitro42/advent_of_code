from itertools import chain, starmap
import operator

import read_input
from common import create_matrix, parse_coords


def parse_input():
    lines = read_input.strings()
    ret = []
    coords_done = False
    coords = []
    inst = []
    for l in lines:
        if not coords_done:
            if l == '':
                coords_done = True
            else:
                coords.append(parse_coords(l))
        else:
            inst.append((l[11], int(l[13:])))

    maxx = max([x for x, _ in coords])
    maxy = max([y for _, y in coords])
    m = create_matrix(maxy + 1, maxx + 1, False)
    for x, y in coords:
        m[y][x] = True

    return m, inst


def print_sheet(board):
    for l in board:
        print(''.join(['#' if v else ' ' for v in l]))
    print()


def fold(m, inst):
    dir, c = inst
    if dir == 'y':
        m = zip(*m)

    m2 = []
    for l in m:
        left = l[:c]
        lright = len(l) - 1 - c
        right = [False] * (c - lright)
        right += l[-lright:][::-1]
        m2.append(starmap(operator.or_, zip(left, right)))

    if dir == 'y':
        m2 = zip(*m2)
    return m2


def solve1(m, instructions) -> None:
    m2 = fold(m, instructions[0])
    print(sum(chain(*m2)))


def solve2(m, instructions) -> None:
    for inst in instructions:
        m = fold(m, inst)
    print_sheet(m)


if __name__ == '__main__':
    input = parse_input()
    m, inst = input
    solve1(*input)
    solve2(*input)
