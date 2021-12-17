import string

import read_input


def parse_input():
    lines = read_input.strings()
    ret = {}
    for l in lines:
        l = l.translate(str.maketrans('', '', string.punctuation))
        l = l.split(' ')
        sue = {l[2]: int(l[3]), l[4]: int(l[5]), l[6]: int(l[7])}
        ret[int(l[1])] = sue
    return ret


detected = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def solve1(input) -> None:
    def check_sue(sue):
        for item in detected:
            if item in sue:
                if detected[item] != sue[item]:
                    return False
        return True

    for idx, sue in input.items():
        if check_sue(sue):
            print(idx)
            return


def solve2(input) -> None:
    def check_sue(sue):
        for item in detected:
            if item in sue:
                if item in ['cats', 'trees']:
                    if detected[item] >= sue[item]:
                        return False
                elif item in ['pomeranians', 'goldfish']:
                    if detected[item] <= sue[item]:
                        return False
                else:
                    if detected[item] != sue[item]:
                        return False
        return True

    for idx, sue in input.items():
        if check_sue(sue):
            print(idx)
            return


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
