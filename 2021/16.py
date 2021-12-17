from __future__ import annotations
import functools
import operator
from dataclasses import dataclass, field
from itertools import islice
from typing import List, Optional

import read_input

SUM = 0
PRODUCT = 1
MIN = 2
MAX = 3
LITERAL = 4
GT = 5
LT = 6
EQ = 7


@dataclass
class Package:
    version: int
    type_id: int
    literal: Optional[int] = None
    packages: List[Package] = field(default_factory=list)


def parse_input():
    line = read_input.string()
    n = len(line) * 4
    bitstr = f'{int(line, 16):0{n}b}'
    package = parse_package(iter(bitstr))
    return package


def bits(it, n):
    return ''.join(islice(it, n))


def parse_literal(it):
    lbits = ''
    while True:
        cont = bits(it, 1) == '1'
        lbits += bits(it, 4)
        if not cont:
            break
    return int(lbits, 2)


def parse_package(it):
    try:
        v = int(bits(it, 3), 2)
    except ValueError:
        return None
    t = int(bits(it, 3), 2)
    if t == LITERAL:
        l = parse_literal(it)
        return Package(v, t, literal=l)
    else:
        lid = bits(it, 1)
        if lid == '0':
            bitcount = int(bits(it, 15), 2)
            pkgbits = islice(it, bitcount)
            pkgs = []
            while True:
                p = parse_package(pkgbits)
                if p is None:
                    break
                pkgs.append(p)
        else:
            b = bits(it, 11)
            pkgcount = int(b, 2)
            pkgs = [parse_package(it) for _ in range(pkgcount)]
        return Package(v, t, packages=pkgs)


def sum_versions(p: Package):
    return p.version + sum([sum_versions(sp) for sp in p.packages])


def print_package(p: Package, indent: int = 0):
    line = '  ' * indent
    line += f'v{p.version}, type_id: {p.type_id}'
    if p.type_id == LITERAL:
        line += f' literal: {p.literal}'
    print(line)
    for sp in p.packages:
        print_package(sp, indent + 1)


def value(p: Package):
    if p.type_id == LITERAL:
        return p.literal
    elif p.type_id == SUM:
        return sum([value(sp) for sp in p.packages])
    elif p.type_id == PRODUCT:
        return functools.reduce(operator.mul, [value(sp) for sp in p.packages])
    elif p.type_id == MIN:
        return min([value(sp) for sp in p.packages])
    elif p.type_id == MAX:
        return max([value(sp) for sp in p.packages])
    elif p.type_id == GT:
        return int(value(p.packages[0]) > value(p.packages[1]))
    elif p.type_id == LT:
        return int(value(p.packages[0]) < value(p.packages[1]))
    elif p.type_id == EQ:
        return int(value(p.packages[0]) == value(p.packages[1]))


if __name__ == '__main__':
    package = parse_input()
    print(sum_versions(package))
    print(value(package))
