import read_input

corruption_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completion_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

openers = ['(', '[', '{', '<']

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def corruption(l):
    opened = ''
    for c in l:
        if len(opened) == 0:
            if c not in openers:
                return corruption_score[c]
            else:
                opened += c
        else:
            if pairs[opened[-1]] == c:
                opened = opened[:-1]
            else:
                if c not in openers:
                    return corruption_score[c]
                else:
                    opened += c
    return opened


def solve1(input) -> None:
    total = 0
    for l in input:
        ret = corruption(l)
        if isinstance(ret, int):
            total += ret

    print(total)


def total_completion_score(s):
    score = 0
    for c in s[::-1]:
        score *= 5
        score += completion_score[pairs[c]]

    return score


def solve2(input) -> None:
    scores = []
    for l in input:
        ret = corruption(l)
        if isinstance(ret, str):
            scores.append(total_completion_score(ret))

    scores.sort()
    print(scores[len(scores) // 2])


if __name__ == '__main__':
    input = read_input.strings()
    # print(input)
    solve1(input)
    solve2(input)
