from copy import deepcopy

import read_input
from common import create_matrix


def parse_input():
    lines = read_input.strings()
    ret = []
    for l in lines:
        ret.append([int(c) for c in l])
    return ret


n = 10

neighbor_offset = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1],
                   [1, 0], [1, 1]]


def neighbor_coords(row, col):
    ret = []
    for no in neighbor_offset:
        r, c = row + no[0], col + no[1]
        if 0 <= r < n and 0 <= c < n:
            ret.append((r, c))
    return ret


def flash_one(m, flashed, row, col):
    for (r, c) in neighbor_coords(row, col):
        if not flashed[r][c]:
            m[r][c] += 1

    m[row][col] = 0
    flashed[row][col] = True


def ready_to_flash(m, flashed):
    ret = []
    for r in range(n):
        for c in range(n):
            if m[r][c] > 9 and not flashed[r][c]:
                ret.append((r, c))
    return ret


def print_cave(m, flashed):
    for r in range(n):
        line = ''.join(
            ['.' if f else str(v) for (v, f) in zip(m[r], flashed[r])])
        print(line)
    print()


def solve1(m) -> None:
    total_flashes = 0
    for step in range(100):
        for r in range(n):
            for c in range(n):
                m[r][c] += 1

        flashed = create_matrix(10, 10, False)
        rtf = ready_to_flash(m, flashed)
        while rtf:
            for coords in rtf:
                flash_one(m, flashed, *coords)
                total_flashes += 1

            rtf = ready_to_flash(m, flashed)
        # print_cave(m, flashed)
    print(total_flashes)


def solve2(m) -> None:
    total_flashes = 0
    step = 1
    while True:
        for r in range(n):
            for c in range(n):
                m[r][c] += 1

        flashed = create_matrix(10, 10, False)
        rtf = ready_to_flash(m, flashed)
        while rtf:
            for coords in rtf:
                flash_one(m, flashed, *coords)
                total_flashes += 1

            rtf = ready_to_flash(m, flashed)
        # print_cave(m, flashed)

        mega_flash = all([all([v == 0 for v in m[r]]) for r in range(n)])
        if mega_flash:
            print(step)
            return
        step += 1


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(deepcopy(input))
    solve2(deepcopy(input))
