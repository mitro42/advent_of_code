import read_input
from common import sign


def parse_input():
    line = read_input.string()
    line = line.replace(',', '').replace('=', ' ').replace('..', ' ')
    p = line.split(' ')
    return (int(p[3]), int(p[4])), (int(p[6]), int(p[7]))


def shoot(target, sx, sy):
    ((x1, x2), (y1, y2)) = target
    x, y = 0, 0
    max_y = 0
    while True:
        x += sx
        y += sy
        # print(x, y, sx, sy, max_y)
        max_y = max(max_y, y)
        sx += sign(-sx)
        sy -= 1
        if x1 <= x <= x2 and y1 <= y <= y2:
            return max_y
        if sx == 0 and not (x1 <= x <= x2):
            return -1
        if sy < 0 and y < y1:
            return -1


def solve1(target) -> None:
    best = 0
    for sx in range(0, abs(target[0][1])):
        for sy in range(0, 500):
            top = shoot(target, sx, sy)
            if top > best:
                # print(sx, sy, top)
                best = top

    print(best)


def solve2(target) -> None:
    count = 0
    for sx in range(0, abs(target[0][1] + 1)):
        for sy in range(target[1][0], 500):
            top = shoot(target, sx, sy)
            if top >= 0:
                # print(sx, sy)
                count += 1

    print(count)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
