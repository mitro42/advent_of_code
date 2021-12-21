from itertools import product, combinations
from typing import List, Tuple, Set

import read_input


def parse_input():
    lines: List[str] = read_input.strings()
    ret = {}
    scanner_id = None
    for l in lines:
        if l == '':
            continue

        if l.startswith('---'):
            scanner_id = int(l.split(' ')[2])
            ret[scanner_id] = set()
            continue

        ret[scanner_id].add(tuple(map(int, l.split(','))))

    return ret


def sequence(v):
    def roll(v):
        return (v[0], v[2], -v[1])

    def turn(v):
        return (-v[1], v[0], v[2])

    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield (v)  #    Yield R
            for i in range(3):  #    Yield TTT
                v = turn(v)
                yield (v)
        v = roll(turn(roll(v)))  # Do RTR


def all_rotations(
        points: List[Tuple[int, int, int]]) -> List[Set[Tuple[int, int, int]]]:
    ret = [set() for i in range(24)]
    for point in points:
        idx = 0
        for rotated in sequence(point):
            ret[idx].add(rotated)
            idx += 1
    return ret


def align_rotation(base, other):
    for p1, p2 in product(base, other):
        ox = p1[0] - p2[0]
        oy = p1[1] - p2[1]
        oz = p1[2] - p2[2]
        new_coords = set([(x + ox, y + oy, z + oz) for (x, y, z) in other])
        if len(base & new_coords) >= 12:
            other.clear()
            other |= new_coords
            return (ox, oy, oz)

    return None


def align(base, other):
    for r in all_rotations(other):
        offset = align_rotation(base, r)
        if offset is not None:
            other.clear()
            other |= r
            return offset
    return None


def solve(scanners) -> None:
    done = set()
    aligned = set([0])
    scanner_coords = []
    while len(done) != len(scanners):
        base = aligned.pop()
        just_aligned = set()
        remaining = set(scanners.keys()) - aligned - done - set([base])
        for other in remaining:
            offset = align(scanners[base], scanners[other])
            if offset is not None:
                just_aligned.add(other)
                scanner_coords.append(offset)
        aligned |= just_aligned
        done.add(base)
        print(done, aligned)

    beacons = set()
    for coords in scanners.values():
        beacons |= coords
    print(len(beacons))

    def dist(p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])

    print(max([dist(p, q) for p, q in combinations(scanner_coords, 2)]))


if __name__ == '__main__':
    input = parse_input()
    solve(input)
