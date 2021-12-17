import functools
import operator
import string
from itertools import product
import numpy as np

import read_input


def parse_input():
    lines = read_input.strings()
    ret = []
    for l in lines:
        parts = l.strip().translate(
            str.maketrans('', '', string.punctuation.replace('-',
                                                             ''))).split(' ')
        _, _, capacity, _, durability, _, flavor, _, texture, _, calories = parts

        ret.append([
            int(capacity),
            int(durability),
            int(flavor),
            int(texture),
            int(calories)
        ])
    return ret


def score(amounts, recipe, ignore_kcals):

    # param_sums = [0] * (len(recipe[0]) - 1)
    # for amount, ingredients in zip(amounts, recipe):
    #     for i in range(len(ingredients) - 1):
    #         param_sums[i] += amount * ingredients[1 + i]
    # print(param_sums)

    m = np.array(recipe)
    param_sums = np.matmul(m.T, amounts)

    if not ignore_kcals and param_sums[-1] != 500:
        return 0

    return functools.reduce(operator.mul, param_sums[:-1]) if all(
        [v > 0 for v in param_sums]) else 0


def solve1(input, ignore_kcals) -> None:
    n = len(input)
    max_amount = 100
    max_score = 0
    for p in product(*[range(max_amount)] * (n - 1)):
        used = sum(p)
        if used > max_amount:
            continue
        amounts = [*p, max_amount - used]
        # print(amounts)
        s = score(amounts, input, ignore_kcals)
        max_score = max(max_score, s)
    print(max_score)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input, True)
    solve1(input, False)
