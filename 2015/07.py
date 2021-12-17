from enum import Enum
from typing import Dict, Union

import read_input


class Op(Enum):
    ASSIGN = 1
    NOT = 2
    AND = 3
    OR = 4
    LSHIFT = 5
    RSHIFT = 6


def validate_wire(name: str) -> None:
    if name.isnumeric():
        raise NotImplementedError(f'Expected wire name, got {name}')


def parse_if_int(s: str):
    if s.isnumeric():
        return int(s)
    return s


def parse_input():
    lines = read_input.strings()
    ret = {}
    for l in lines:
        expression, target = l.strip().split(' -> ')
        if target in ret:
            raise RuntimeError('Multiple assignments to ' + target)
        if 'NOT' in expression:
            operand = expression[4:]
            validate_wire(operand)
            ret[target] = [Op.NOT, operand]
        elif 'AND' in expression or 'OR' in expression:
            lhs, op, rhs = expression.split(' ')
            lhs = parse_if_int(lhs)
            rhs = parse_if_int(rhs)
            ret[target] = [Op[op], lhs, rhs]
        elif 'LSHIFT' in expression or 'RSHIFT' in expression:
            lhs, op, rhs = expression.split(' ')
            lhs = parse_if_int(lhs)
            rhs = parse_if_int(rhs)
            ret[target] = [Op[op], lhs, rhs]
        else:
            expression = parse_if_int(expression)
            ret[target] = [Op.ASSIGN, expression]

    return ret


def get(values: Dict[str, int], key: Union[int, str]):
    if isinstance(key, int):
        return key

    return values.get(key, None)


def solve1(input: dict) -> dict:
    values = {}
    while 'a' not in values:
        for target, exp in input.items():
            if target in values:
                continue
            op = exp[0]
            if op == Op.ASSIGN:
                val = get(values, exp[1])
                if val is not None:
                    values[target] = val
            elif op == Op.NOT:
                if exp[1] in values:
                    values[target] = values[exp[1]] ^ (2**16 - 1)
            elif op == Op.AND:
                lhs = get(values, exp[1])
                rhs = get(values, exp[2])
                if lhs is not None and rhs is not None:
                    values[target] = lhs & rhs
            elif op == Op.OR:
                lhs = get(values, exp[1])
                rhs = get(values, exp[2])
                if lhs is not None and rhs is not None:
                    values[target] = lhs | rhs
            elif op == Op.LSHIFT:
                if exp[1] in values:
                    values[target] = values[exp[1]] << exp[2]
            elif op == Op.RSHIFT:
                if exp[1] in values:
                    values[target] = values[exp[1]] >> exp[2]

    print(values['a'])
    return values


def solve2(input: dict) -> None:
    values = solve1(input)
    input['b'] = [Op.ASSIGN, values['a']]
    solve1(input)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    # solve1(input)
    solve2(input)
