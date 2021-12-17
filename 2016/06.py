from collections import Counter

import read_input


def solve1(input) -> None:
    input_t = zip(*input)
    msg = ''
    for l in input_t:
        counter = Counter(l)
        msg += counter.most_common(1)[0][0]
    print(msg)


def solve2(input) -> None:
    input_t = zip(*input)
    msg = ''
    for l in input_t:
        counter = Counter(l)
        msg += counter.most_common()[-1][0]
    print(msg)


if __name__ == '__main__':
    input = read_input.strings()
    # print(input)
    solve1(input)
    solve2(input)
