import hashlib


def solve1(input: str) -> None:
    i = 1
    while True:
        md5 = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if md5.startswith('00000'):
            print(i)
            return
        i += 1


def solve2(input: str) -> None:
    i = 1
    while True:
        md5 = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if md5.startswith('000000'):
            print(i)
            return
        i += 1


if __name__ == '__main__':
    input = 'iwrupvqb'
    # print(input)
    solve1(input)
    solve2(input)
