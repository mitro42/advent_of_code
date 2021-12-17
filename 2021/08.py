from typing import List, Any

import read_input


def ss(s):
    return ''.join(sorted(s))


def parse_input() -> List[Any]:
    lines = read_input.strings(sep=' ')
    ret = []
    for l in lines:
        ret.append((l[:10], l[11:]))
    return ret


def solve1(input) -> None:
    total = 0
    for l in input:
        line_output = [len(v) for v in l[1]]
        total += sum([v in [2, 3, 4, 7] for v in line_output])
    print(total)


def get_codes(l):
    d = [None] * 10
    d[1] = [set(v) for v in l if len(v) == 2][0]
    d[4] = [set(v) for v in l if len(v) == 4][0]
    d[7] = [set(v) for v in l if len(v) == 3][0]
    d[8] = [set(v) for v in l if len(v) == 7][0]

    c690 = [set(v) for v in l if len(v) == 6]
    for v in c690:
        if not d[1].issubset(v):
            d[6] = v
            break
    c90 = [v for v in c690 if v != d[6]]
    if d[4].issubset(c90[0]):
        d[9] = c90[0]
        d[0] = c90[1]
    else:
        d[9] = c90[1]
        d[0] = c90[0]

    c235 = [set(v) for v in l if len(v) == 5]
    for v in c235:
        if d[1].issubset(v):
            d[3] = v
            break
    c25 = [v for v in c235 if v != d[3]]

    if c25[0].issubset(d[9]):
        d[5] = c25[0]
        d[2] = c25[1]
    else:
        d[5] = c25[1]
        d[2] = c25[0]

    codes = {ss(list(v)): k for (k, v) in enumerate(d)}

    return codes


def solve2(input) -> None:
    total = 0
    for l in input:
        codes = get_codes(l[0])
        line_output = [codes[ss(v)] for v in l[1]]
        v = int(''.join([str(d) for d in line_output]))
        total += v
    print(total)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
