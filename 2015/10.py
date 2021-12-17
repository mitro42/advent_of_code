from itertools import takewhile


def look_and_say(s: str):
    ret = []
    while s:
        pref = list(takewhile(lambda c: c == s[0], s))
        s = s[len(pref):]
        ret += [str(len(pref)), pref[0]]

    return ''.join(ret)


def look_and_say2(s: str):
    ret = []
    idx = 0
    while idx < len(s):
        pref = list(takewhile(lambda c: c == s[idx], s[idx:]))
        idx += len(pref)
        # s=s[len(pref):]
        ret += f'{len(pref)}{pref[0]}'

    return ''.join(ret)


def look_and_say3(s: str):
    ret = []
    idx = 0
    while idx < len(s):
        count = 0
        j = idx
        while j < len(s) and s[j] == s[idx]:
            j += 1

        ret += f'{j-idx}{s[idx]}'
        idx = j

    return ''.join(ret)


def solve(input: str, n) -> None:
    # start = dt.datetime.now()
    for i in range(n):
        input = look_and_say3(input)
    print(len(input))
    # end = dt.datetime.now()
    # print(end - start)


if __name__ == '__main__':
    input = "1113222113"
    # print(input)
    solve(input, 40)
    solve(input, 50)
