import re
from itertools import product

seq = [
    'abc', 'bcd', 'cde', 'def', 'efg', 'pqr', 'qrs', 'rts', 'tsu', 'suv',
    'uvw', 'vwx', 'wxy', 'xyz'
]
chars = 'abcdefghjkmnpqrstuvwxyz'
first_chars = 'vwxyzabcdefghjkmnpqrstu'


def create_password(p):
    *c, seq, seq_pos, capital1, capital2 = p
    if capital1 < 3:
        c[capital1] = c[capital1].upper()
    elif capital1 == 3:
        seq = seq[0].upper() + seq[1:]
    elif capital1 == 4:
        seq = seq[:2] + seq[2].upper()

    if capital2 < 3:
        c[capital2] = c[capital2].upper()
    elif capital2 == 3:
        seq = seq[0].upper() + seq[1:]
    elif capital2 == 4:
        seq = seq[:2] + seq[2].upper()

    c.insert(seq_pos, seq)
    ret = ''.join(c)
    final_capitals = [c for c in ret if c.isupper()]
    if final_capitals[0] == final_capitals[1]:
        return None
    ret = re.sub('([A-Z])', lambda pat: pat.group(1).lower() * 2, ret)
    return ret


def solve1(input: str):
    best = "zzzzzzzzzzzzzzzzzzzz"
    for p in product(
            *[first_chars, chars, chars, seq,
              range(4),
              range(5),
              range(5)]):
        if p[5] == p[6]:
            continue
        pw = create_password(p)
        if pw is not None and pw > input:
            if pw < best:
                best = pw
                # print(best)
    print(best)


if __name__ == '__main__':
    input = "vzbxxyzz"
    print(input)
    solve1(input)
    # solve2(input)
