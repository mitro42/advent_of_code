from enum import Enum
from typing import List, Any

import read_input
from common import sign


class Direction(Enum):
    N = 1,
    E = 2,
    S = 3,
    W = 4


def turn(d: Direction, turn: str) -> Direction:
    if turn == 'R':
        return {
            Direction.N: Direction.E,
            Direction.E: Direction.S,
            Direction.S: Direction.W,
            Direction.W: Direction.N,
        }[d]
    else:
        return {
            Direction.N: Direction.W,
            Direction.E: Direction.N,
            Direction.S: Direction.E,
            Direction.W: Direction.S,
        }[d]


def move(x, y, dir, dist):
    if dir == Direction.N:
        return x, y - dist
    if dir == Direction.E:
        return x + dist, y
    if dir == Direction.S:
        return x, y + dist
    if dir == Direction.W:
        return x - dist, y


def parse_input() -> List[Any]:
    line = read_input.string()
    ret = [(i[0], int(i[1:])) for i in line.split(', ')]
    return ret


def solve1(input) -> None:
    x, y = 0, 0
    dir = Direction.N
    for (next_turn, dist) in input:
        dir = turn(dir, next_turn)
        x, y = move(x, y, dir, dist)

    print(abs(x) + abs(y))


def section_points(x1, y1, x2, y2):
    dx, dy = sign(x2 - x1), sign(y2 - y1)
    ret = []
    while x1 != x2 or y1 != y2:
        ret.append((x1, y1))

        x1 += dx
        y1 += dy

    ret.append((x2, y2))
    return ret[1:]


def solve2(input) -> None:
    x, y = 0, 0
    dir = Direction.N
    visited = set([(x, y)])
    for (next_turn, dist) in input:
        dir = turn(dir, next_turn)
        x0, y0 = x, y
        x, y = move(x, y, dir, dist)
        section = section_points(x0, y0, x, y)
        for p in section:
            if p in visited:
                print(abs(p[0]) + abs(p[1]))
                return
        else:
            visited |= set(section)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
