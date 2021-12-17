from typing import Any, List


def parse_coords(s: str) -> List[int]:
    return list(map(int, s.split(',')))


def create_matrix(rows: int, cols: int, value: Any) -> List[List[Any]]:
    m = []
    for j in range(rows):
        m.append([value] * cols)
    return m


def sign(n):
    if n == 0:
        return 0
    elif n > 0:
        return 1
    else:
        return -1