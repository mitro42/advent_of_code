from __future__ import annotations
from itertools import islice, takewhile
from typing import Optional
import math
from dataclasses import dataclass
from copy import deepcopy

import read_input


@dataclass
class SN:
    p: Optional[SN]
    i: int
    l: Optional[SN]
    r: Optional[SN]

    @property
    def is_snail(self):
        return self.i == -1

    def magnitude(self) -> int:
        if self.is_snail:
            return 3 * self.l.magnitude() + 2 * self.r.magnitude()
        else:
            return self.i

    def __str__(self):
        if self.is_snail:
            return f'[{self.l},{self.r}]'
        else:
            return str(self.i)

    def add(self, other: SN) -> SN:
        sn = SN(None, -1, self, other)
        self.p = sn
        other.p = sn
        reduce(sn)
        return sn

    def add_left(self, n):
        if self.is_snail:
            self.l.add_left(n)
        else:
            self.i += n

    def add_right(self, n):
        if self.is_snail:
            self.r.add_right(n)
        else:
            self.i += n

    def find(self, depth) -> Optional[SN]:
        if not self.is_snail:
            return None

        if depth == 0:
            return self
        else:
            l = self.l.find(depth - 1)
            if l is not None:
                return l
            return self.r.find(depth - 1)

    def find_splittable(self) -> Optional[SN]:
        if not self.is_snail:
            if self.i >= 10:
                return self
            else:
                return None

        lsplittabe = self.l.find_splittable()
        if lsplittabe is not None:
            return lsplittabe

        return self.r.find_splittable()


def explode(sn):
    ex = sn.find(4)
    if ex is None:
        return False
    if ex == ex.p.l:
        ex.p.r.add_left(ex.r.i)
        p = ex.p
        while p.p is not None and p is p.p.l:
            p = p.p
        if p.p is not None:
            p.p.l.add_right(ex.l.i)
        ex.p.l = SN(ex.p, 0, None, None)
    else:
        ex.p.l.add_right(ex.l.i)
        p = ex.p
        while p.p is not None and p is p.p.r:
            p = p.p
        if p.p is not None:
            p.p.r.add_left(ex.r.i)
        ex.p.r = SN(ex.p, 0, None, None)
    return True


def split(sn):
    s = sn.find_splittable()
    if s is None:
        return False
    sn = SN(s.p, -1, None, None)
    l = SN(sn, int(math.floor(s.i / 2)), None, None)
    r = SN(sn, int(math.ceil(s.i / 2)), None, None)
    sn.l = l
    sn.r = r
    if s is s.p.l:
        s.p.l = sn
    else:
        s.p.r = sn
    return True


def reduce(sn):
    while True:
        while explode(sn):
            pass
        if not split(sn):
            break


def parse_sn(it, p=None):
    c = next(islice(it, 1))
    if c != '[':
        v = c + ''.join(takewhile(lambda x: x.isnumeric(), it))
        return SN(p, int(v), None, None)
    else:
        sn = SN(p, -1, None, None)
        lhs = parse_sn(it, sn)
        rhs = parse_sn(it, sn)
        try:
            next(it)  # ]
        except StopIteration:
            pass

        sn.l = lhs
        sn.r = rhs
        return sn


def parse_input():
    lines = read_input.strings()
    ret = []
    for l in lines:
        it = iter(l)
        sn = parse_sn(it)
        ret.append(sn)
    return ret


def solve1(input) -> None:
    s = input[0]
    for sn in input[1:]:
        s = s.add(sn)
    print(s.magnitude())


def solve2(input) -> None:
    max_magn = 0
    for sn1 in input:
        for sn2 in input:
            if sn1 is sn2:
                continue
            s1 = deepcopy(sn1)
            s2 = deepcopy(sn2)
            max_magn = max(max_magn, s1.add(s2).magnitude())
    print(max_magn)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    input = parse_input()
    solve2(input)
