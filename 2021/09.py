from typing import List, Any

import read_input


class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.weight = [1] * n

    def root(self, idx: int) -> int:
        while idx != self.id[idx]:
            self.id[idx] = self.id[self.id[idx]]
            idx = self.id[idx]
        return idx

    def join(self, a: int, b: int) -> None:
        p = self.root(a)
        q = self.root(b)

        if p != q:
            if self.weight[p] > self.weight[q]:
                p, q = q, p

            self.id[p] = self.id[q]
            self.weight[q] += self.weight[p]

    def same(self, a: int, b: int) -> bool:
        return self.root(a) == self.root(b)

    def get_weight(self, a: int) -> int:
        return self.weight[self.root(a)]


neighbor_coords = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def parse_input() -> List[Any]:
    lines = read_input.strings()
    ret = []
    for l in lines:
        ret.append([int(d) for d in l])
    return ret


def lowest_neighbor(m, row, col):
    rows = len(m)
    cols = len(m[0])
    heights = []
    for nc in neighbor_coords:
        r = row + nc[0]
        c = col + nc[1]
        if 0 <= r < rows and 0 <= c < cols:
            heights.append(m[r][c])
    return min(heights)


def solve1(m) -> None:
    rows = len(m)
    cols = len(m[0])
    total = 0
    for r in range(rows):
        for c in range(cols):
            if m[r][c] < lowest_neighbor(m, r, c):
                total += m[r][c] + 1
    print(total)


def solve2(m) -> None:
    rows = len(m)
    cols = len(m[0])
    uf = UnionFind(rows * cols)
    total = 0
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == 9:
                continue
            id = row * cols + col
            for nc in neighbor_coords:
                r = row + nc[0]
                c = col + nc[1]
                if 0 <= r < rows and 0 <= c < cols:
                    if m[r][c] != 9:
                        uf.join(id, r * cols + c)

    basin_sizes = {}
    for row in range(rows):
        for col in range(cols):
            id = row * cols + col
            basin_sizes[uf.root(id)] = uf.get_weight(id)
    big3 = sorted(basin_sizes.values())[-3:]
    print(big3[0] * big3[1] * big3[2])


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
