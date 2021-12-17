from collections import Counter

import read_input


def parse_input():
    g = {}
    lines = read_input.strings(sep='-')
    for (s, e) in lines:
        if s in g:
            g[s].append(e)
        else:
            g[s] = [e]

        if e in g:
            g[e].append(s)
        else:
            g[e] = [s]
    return g


def can_visit1(node, p):
    return node.isupper() or node not in [n for (n, i) in p]


def solve1(g) -> None:
    paths = set()
    cp = []
    cp.append(('start', -1))
    while cp:
        node, idx = cp.pop()
        if node == 'end':
            paths.add(str(cp))
            continue

        if idx + 1 < len(g[node]):
            next_node = g[node][idx + 1]
            if not can_visit1(next_node, cp):
                cp.append((node, idx + 1))
                continue

            cp.append((node, idx + 1))
            cp.append((next_node, -1))

    print(len(paths))


def has_double_lower(counter):
    for node, count in counter.most_common():
        if node.islower() and count >= 2:
            return True
    return False


def can_visit2(node, p):
    if node.isupper():
        return True
    if node == 'start':
        return False

    visited = Counter([n for (n, i) in p])

    if has_double_lower(visited) and node in visited.keys():
        return False

    return True


def solve2(g) -> None:
    paths = set()
    cp = []
    cp.append(('start', -1))
    while cp:
        node, idx = cp.pop()
        if node == 'end':
            paths.add(', '.join([n for (n, idx) in cp]))
            continue

        if idx + 1 < len(g[node]):
            next_node = g[node][idx + 1]

            if not can_visit2(next_node, cp + [(node, idx)]):
                cp.append((node, idx + 1))
                continue

            cp.append((node, idx + 1))
            cp.append((next_node, -1))

    print(len(paths))


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
