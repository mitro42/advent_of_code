import read_input
from common import create_matrix


def print_pic(board):
    for l in board:
        print(''.join(['#' if v else '.' for v in l]))
    print()


def parse_input():
    lines = iter(read_input.strings())
    algo = []

    for l in lines:
        if l != '':
            algo += [int(c == '#') for c in l]
        else:
            break
    pic = []
    for l in lines:
        pic.append([int(c == '#') for c in l])
    return algo, pic


mask_coords = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1],
               [1, 0], [1, 1]]


def get_square_value(pic, row, col):
    ret = 0
    for ro, co in mask_coords:
        ret *= 2
        ret += pic[row + ro][col + co]
    return ret


def expand(pic, b):
    cols = len(pic[0])
    ret = []
    ret.append([b] * (cols + 2))
    for l in pic:
        ret.append([b] + l + [b])
    ret.append([b] * (cols + 2))
    return ret


def crop(pic):
    rows = len(pic)
    for i in range(1, rows - 1):
        pic[i] = pic[i][1:-1]
    del pic[-1]
    del pic[0]


def enhance(algo, pic, b):
    pic = expand(pic, b)
    pic = expand(pic, b)
    pic = expand(pic, b)
    rows = len(pic)
    cols = len(pic[0])

    np = create_matrix(rows, cols, b)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            v = get_square_value(pic, r, c)
            np[r][c] = algo[v]
    crop(np)
    return np


def solve(algo, pic, n) -> None:
    pic = enhance(algo, pic, 0)
    for _ in range(1, n):
        pic = enhance(algo, pic, pic[0][0])

    print(sum([sum(l) for l in pic]))


if __name__ == '__main__':
    algo, pic = parse_input()
    # print_pic(pic)
    solve(algo, pic, 2)
    solve(algo, pic, 50)
