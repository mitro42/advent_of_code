import re

import read_input


def solve1(input):
    original_char_count = sum(map(len, input))
    decoded = []
    hex_re = re.compile(r'\\x[0-9a-fA-F][0-9a-fA-F]')
    for l in input:
        l = l[1:-1]
        l = l.replace('\\"', '"')
        l = hex_re.sub('A', l)
        l = l.replace('\\\\', '\\')
        decoded.append(l)
    decoded_char_count = sum(map(len, decoded))
    print(original_char_count - decoded_char_count)


def solve2(input) -> None:
    original_char_count = sum(map(len, input))
    encoded = []
    for l in input:
        l = l.replace('\\', '\\\\')
        l = l.replace('"', '\\"')
        l = '"' + l + '"'
        encoded.append(l)
    encoded_char_count = sum(map(len, encoded))
    print(encoded_char_count - original_char_count)


if __name__ == '__main__':
    input = read_input.strings()
    # print(input)
    solve1(input)
    solve2(input)
