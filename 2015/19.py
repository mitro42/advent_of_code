import read_input


def parse_input():
    lines = read_input.strings(sep=' ')
    # subs = defaultdict(list)
    subs = []
    subs_done = False
    for l in lines:
        if l == ['']:
            subs_done = True
            continue
        if not subs_done:
            # subs[l[0]].append(l[2])
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


# def solve2(subs, target) -> None:
#     molecules = set([target])
#     closed = set()

#     step = 0
#     from_e = set([m for (x, m) in subs if x == 'e'])
#     subs = [(x, m) for (x, m) in subs if x != 'e']
#     while len(from_e & molecules) == 0:
#         new_closed = set()
#         new_molecules = set()
#         for old in molecules - closed:
#             for s in subs:
#                 new_molecules |= create_new_molecules((s[1], s[0]), old)
#             new_closed.add(old)
#         closed |= new_closed
#         molecules |= new_molecules
#         print(f'molecules: {len(molecules)}, closed: {len(closed)}')

#         step += 1
#     print(step + 1)

if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(*input)
    # solve2(*input)
