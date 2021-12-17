import read_input


def solve1(input: str) -> None:
    coords = set()
    x, y = 0, 0
    for dir in input:
        if dir == '<':
            y -= 1
        elif dir == '>':
            y += 1
        elif dir == '^':
            x -= 1
        elif dir == 'v':
            x += 1
        coords.add((x, y))
    print(len(coords))


def solve2(input: str) -> None:
    coords = set()
    sx, sy = 0, 0
    rx, ry = 0, 0
    for i, dir in enumerate(input):
        x, y = (sx, sy) if i % 2 == 0 else (rx, ry)

        if dir == '<':
            y -= 1
        elif dir == '>':
            y += 1
        elif dir == '^':
            x -= 1
        elif dir == 'v':
            x += 1
        coords.add((x, y))

        if i % 2 == 0:
            sx, sy = x, y
        else:
            rx, ry = x, y
    print(len(coords))


if __name__ == '__main__':
    input = read_input.string()
    # print(input)
    solve1(input)
    solve2(input)
