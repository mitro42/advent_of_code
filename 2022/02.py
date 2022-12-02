from typing import List, Tuple

import read_input


def parse_input():
    return read_input.strings(sep=' ')


def solve1(lines: List[Tuple[str, str]]) -> None:
    plan = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
        'X': 'R',
        'Y': 'P',
        'Z': 'S',
    }
    rounds = [(plan[a], plan[b]) for (a, b) in lines]

    value = {'R': 1, 'P': 2, 'S': 3}
    round_score = {
        ('R', 'R'): 3,
        ('R', 'P'): 0,
        ('R', 'S'): 6,
        ('P', 'R'): 6,
        ('P', 'P'): 3,
        ('P', 'S'): 0,
        ('S', 'R'): 0,
        ('S', 'P'): 6,
        ('S', 'S'): 3,
    }

    score = 0
    for round in rounds:
        score += value[round[1]] + round_score[(round[1], round[0])]

    print(score)


def solve2(lines: List[Tuple[str, str]]) -> None:
    plan = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
        'X': 'L',
        'Y': 'D',
        'Z': 'W',
    }

    rounds = [(plan[a], plan[b]) for (a, b) in lines]

    outcome_value = {'W': 6, 'D': 3, 'L': 0}
    value = {'R': 1, 'P': 2, 'S': 3}

    step = {
        ('W', 'R'): 'P',
        ('W', 'P'): 'S',
        ('W', 'S'): 'R',
        ('D', 'R'): 'R',
        ('D', 'P'): 'P',
        ('D', 'S'): 'S',
        ('L', 'R'): 'S',
        ('L', 'P'): 'R',
        ('L', 'S'): 'P',
    }

    score = 0
    for round in rounds:
        score += outcome_value[round[1]] + value[step[(round[1], round[0])]]

    print(score)


if __name__ == '__main__':
    input = parse_input()
    solve1(input)
    solve2(input)
