import read_input


def parse_input():
    lines = read_input.strings(sep=' ')
    subs = []
    subs_done = False
    for l in lines:
        if l == ['']:
            subs_done = True
            continue
        if not subs_done:
            subs.append((l[0], l[2]))
        else:
            molecule = l[0]

    return subs, molecule


def create_new_molecules(sub, molecule):
    ret = set()
    idx = molecule.find(sub[0])
    while idx != -1:
        m = molecule[:idx] + sub[1] + molecule[idx + len(sub[0]):]
        ret.add(m)
        idx = molecule.find(sub[0], idx + 1)
    return ret


def solve1(subs, molecule) -> None:
    results = set()
    for s in subs:
        results |= create_new_molecules(s, molecule)
    print(len(results))


def solve2(subs, target) -> None:
    max_sub_len = max([len(rule[1]) for rule in subs])
    reductions = {v: k for k, v in subs}

    count = 0
    while target != 'e':
        for i in range(len(target), 0, -1):
            for l in range(1, max_sub_len + 1):
                rhs = target[i - l:i]
                if rhs in reductions:
                    count += 1
                    target = reductions[rhs].join(target.rsplit(rhs, 1))
                    # print(f'{count}: {rhs} => {reductions[rhs]}')
                    # print(target)
                    break
            else:
                continue
            break
    print(count)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(*input)
    solve2(*input)
