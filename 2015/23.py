from typing import List, Any

import read_input


def parse_input() -> List[Any]:
    lines = read_input.strings(sep=' ')
    ret = []
    for l in lines:
        op = l[0]
        if op == 'jmp':
            ret.append((op, int(l[1])))
        elif op in ['jio', 'jie']:
            ret.append((op, l[1][0], int(l[2])))
        else:
            ret.append((op, l[1]))
    return ret


def solve(p, registers) -> None:
    r = registers
    ip = 0
    while ip < len(p):
        cmd = p[ip]
        op = cmd[0]
        if op == 'hlf':
            r[cmd[1]] //= 2
            ip += 1
        elif op == 'tpl':
            r[cmd[1]] *= 3
            ip += 1
        elif op == 'inc':
            r[cmd[1]] += 1
            ip += 1
        elif op == 'jmp':
            ip += cmd[1]
        elif op == 'jie':
            if r[cmd[1]] % 2 == 0:
                ip += cmd[2]
            else:
                ip += 1
        elif op == 'jio':
            if r[cmd[1]] == 1:
                ip += cmd[2]
            else:
                ip += 1
    print(r['b'])


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve(input, {'a': 0, 'b': 0})
    solve(input, {'a': 1, 'b': 0})
