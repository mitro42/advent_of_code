from itertools import chain, permutations

import read_input


def parse_input():
    lines = read_input.strings()
    ret = {}
    for l in lines:
        parts = l.rstrip('.').split(' ')
        score = int(parts[3]) * (-1 if parts[2] == 'lose' else 1)
        ret[(parts[0], parts[-1])] = score
    return ret


def solve1(input) -> None:
    names = sorted(list(set(chain(*input.keys()))))
    n = len(names)
    best_score = 0
    for p in permutations(names):
        score = 0
        for i in range(n):
            score += input[(p[i], p[(i + 1) % n])]
            score += input[(p[i], p[(i - 1) % n])]
        best_score = max(best_score, score)
    print(best_score)


def solve2(input) -> None:
    names = sorted(list(set(chain(*input.keys()))))
    for name in names:
        input[('X', name)] = 0
        input[(name, 'X')] = 0
    solve1(input)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
