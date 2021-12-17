import hashlib


def solve1(input: str) -> None:
    i = 0
    pw = ''
    while True:
        md5 = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if md5.startswith('00000'):
            # print(md5[5])
            pw += md5[5]
            if len(pw) == 8:
                break
        i += 1
    print(pw)


def solve2(input: str) -> None:
    i = -1
    pw = list('.' * 8)
    while True:
        i += 1
        md5 = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if md5.startswith('00000'):
            idx = md5[5]
            if idx not in '01234567':
                continue
            idx = int(idx)
            if pw[idx] != '.':
                continue

            pw[idx] = md5[6]
            # print(''.join(pw))
            if '.' not in pw:
                break
    print(''.join(pw))


if __name__ == '__main__':
    # input = 'abc'
    input = 'wtnhxymk'
    # print(input)
    solve1(input)
    solve2(input)
