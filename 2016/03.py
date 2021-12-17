from itertools import chain
from typing import List, Any

import read_input


def parse_input() -> List[Any]:
    lines = read_input.strings(strip=False)
    ret = []
    for l in lines:
        ret.append((int(l[:5]), int(l[5:10]), int(l[10:])))
    return ret


def valid_triangle(sides):
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True


def solve1(input) -> None:
    sol = sum(map(valid_triangle, input))
    print(sol)


def trigrouper(iterable):
    args = [iter(iterable)] * 3
    return zip(*args)


def solve2(input) -> None:
    input_t = zip(*input)
    single_list_input = chain(*input_t)
    sol = sum(map(valid_triangle, trigrouper(single_list_input)))
    print(sol)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
