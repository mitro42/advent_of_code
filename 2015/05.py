from typing import List

import read_input


def nice1(s: str) -> bool:
    wowel_count = sum([c in 'aeiou' for c in s])
    if wowel_count < 3:
        return False

    repeated_ok = False
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            repeated_ok = True
        if s[i:i + 2] in ['ab', 'cd', 'pq', 'xy']:
            return False

    return repeated_ok


def solve1(input: List[str]) -> None:
    print(sum([nice1(l) for l in input]))


def nice2(s: str) -> bool:
    double_pair_ok = False
    seen = {}
    for i in range(0, len(s) - 1):
        prev_pos = seen.get(s[i:i + 2], -1)
        if prev_pos >= 0 and i - 1 != prev_pos:
            double_pair_ok = True
            break

        if prev_pos == -1:
            seen[s[i:i + 2]] = i

    one_gap_ok = False
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2]:
            one_gap_ok = True

    # print(double_pair_ok and one_gap_ok)
    return double_pair_ok and one_gap_ok


def solve2(input: List[str]) -> None:
    print(sum([nice2(l) for l in input]))


if __name__ == '__main__':
    input = read_input.strings()
    # print(input)
    solve1(input)
    solve2(input)
