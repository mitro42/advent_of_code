from collections import Counter
from typing import List, Any
import string

import read_input


def parse_input() -> List[Any]:
    lines = read_input.strings()
    ret = []
    for l in lines:
        l = l[:-1]
        room_sector, checksum = l.split('[')
        room, _, sector = room_sector.rpartition('-')
        ret.append((room, int(sector), checksum))
    return ret


def is_valid_room(room, checksum):
    counter = Counter(sorted(room.replace('-', '')))
    return checksum == ''.join([c for c, _ in counter.most_common(5)])


def solve1(input) -> None:
    total = 0
    for room, sector, checksum in input:
        if is_valid_room(room, checksum):
            total += sector

    print(total)


def decode(room, sector):
    rotate = sector % 26
    abc = string.ascii_lowercase
    abc_rot = abc[rotate:] + abc[:rotate]
    tr = str.maketrans(abc, abc_rot)
    return room.translate(tr)


def solve2(input) -> None:
    names = []
    for room, sector, checksum in input:
        if is_valid_room(room, checksum):
            name = decode(room, sector)
            if 'north' in name:
                print(name, sector)
                return
            # names.append(name)

    # print('\n'.join(sorted(names)))


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
