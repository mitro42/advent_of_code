from itertools import chain
from typing import Any, List

import read_input
from common import parse_coords

N = 1000


def parse_input() -> List[Any]:
    lines = read_input.strings()
    ret = []
    for l in lines:
        if l.startswith('turn'):
            l = l[5:]
        l = l.split(' ')
        ret.append([l[0], parse_coords(l[1]), parse_coords(l[3])])
    return ret


def switch1(lights: List[List[bool]], command: str, tl: List[int],
            br: List[int]) -> None:
    if command == 'on':

        def f(x, y):
            lights[y][x] = True
    elif command == 'off':

        def f(x, y):
            lights[y][x] = False
    else:

        def f(x, y):
            lights[y][x] = not lights[y][x]

    for x in range(tl[0], br[0] + 1):
        for y in range(tl[1], br[1] + 1):
            f(x, y)


def solve1(input: List[Any]) -> None:
    lights = []
    for i in range(N):
        lights.append([False] * N)

    for l in input:
        switch1(lights, *l)

    print(sum(chain(*lights)))


def switch2(lights: List[List[int]], command: str, tl: List[int],
            br: List[int]) -> None:
    if command == 'on':

        def f(x, y):
            lights[y][x] += 1
    elif command == 'off':

        def f(x, y):
            if lights[y][x] > 0:
                lights[y][x] -= 1
    else:

        def f(x, y):
            lights[y][x] += 2

    for x in range(tl[0], br[0] + 1):
        for y in range(tl[1], br[1] + 1):
            f(x, y)


def solve2(input: List[Any]) -> None:
    lights = []
    for i in range(N):
        lights.append([0] * N)

    for l in input:
        switch2(lights, *l)

    print(sum(chain(*lights)))


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
