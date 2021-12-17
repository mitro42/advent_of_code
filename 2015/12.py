import read_input


def sum_json1(v):
    if isinstance(v, int):
        return v
    elif isinstance(v, list):
        return sum([sum_json1(e) for e in v])
    elif isinstance(v, dict):
        return sum([sum_json1(o) for o in v.values()])
    else:
        return 0


def sum_json2(v):
    if isinstance(v, int):
        return v
    elif isinstance(v, list):
        children = [sum_json2(e) for e in v]
        return sum(children)
    elif isinstance(v, dict):
        has_red = 'red' in v.values()
        if has_red:
            return 0
        else:
            children = [sum_json2(o) for o in v.values()]
            return sum(children)
    elif isinstance(v, str):
        return 0
    else:
        raise RuntimeError('What now?')


def solve1(input) -> None:
    print(sum_json1(input))


def solve2(input) -> None:
    print(sum_json2(input))


if __name__ == '__main__':
    input = read_input.parse_json()
    # print(input)
    solve1(input)
    solve2(input)
