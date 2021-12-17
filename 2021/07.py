import read_input


def cost1(input, target):
    per_sub = [abs(target - input[i]) for i in range(len(input))]
    return sum(per_sub)


def cost2(input, target):
    per_sub = [
        abs(target - input[i]) * (abs(target - input[i]) + 1) // 2
        for i in range(len(input))
    ]
    return sum(per_sub)


def solve(input, cost) -> None:
    costs = [
        cost(input, target) for target in range(min(input),
                                                max(input) + 1)
    ]

    print(min(costs))


def solve1(input) -> None:
    solve(input, cost1)


def solve2(input) -> None:
    solve(input, cost2)


if __name__ == '__main__':
    input = read_input.numbers(single_line=True)
    # print(input)
    solve1(input)
    solve2(input)
