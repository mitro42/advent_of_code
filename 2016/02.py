import read_input

keypad = [
    '00000',
    '01230',
    '04560',
    '07890',
    '00000',
]
keypad2 = [
    '0000000',
    '0001000',
    '0023400',
    '0567890',
    '00ABC00',
    '000D000',
    '0000000',
]


def move(x, y, dir, layout):
    x0, y0 = x, y
    if dir == 'U':
        x, y = x, y - 1
    if dir == 'D':
        x, y = x, y + 1
    if dir == 'L':
        x, y = x - 1, y
    if dir == 'R':
        x, y = x + 1, y

    if layout[y][x] == '0':
        return x0, y0
    else:
        return x, y


def solve1(input) -> None:
    x, y = 2, 2
    code = ''
    for line in input:
        for dir in line:
            x, y = move(x, y, dir, keypad)
        code += keypad[y][x]
    print(code)


def solve2(input) -> None:
    x, y = 1, 3
    code = ''
    for line in input:
        for dir in line:
            x, y = move(x, y, dir, keypad2)
        code += keypad2[y][x]
    print(code)


if __name__ == '__main__':
    input = read_input.strings()
    # print(input)
    solve1(input)
    solve2(input)
