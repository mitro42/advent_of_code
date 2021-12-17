from copy import deepcopy
from dataclasses import dataclass

import read_input


@dataclass
class Reindeer:
    name: str
    speed: int
    move_duration: int
    rest_duration: int
    remaining: int = 0
    state: str = 'move'

    def __post_init__(self):
        self.remaining = self.move_duration

    def step(self):
        self.remaining -= 1
        if self.state == 'move':
            if self.remaining == 0:
                self.state = 'rest'
                self.remaining = self.rest_duration
            return self.speed
        else:
            if self.remaining == 0:
                self.state = 'move'
                self.remaining = self.move_duration
            return 0


def parse_input():
    lines = read_input.strings()
    ret = []
    for l in lines:
        parts = l.rstrip('.').split(' ')
        ret.append(
            Reindeer(name=parts[0],
                     speed=int(parts[3]),
                     move_duration=int(parts[6]),
                     rest_duration=int(parts[13])))
    return ret


def solve1(input) -> None:
    distances = {d.name: 0 for d in input}
    for i in range(2503):
        for d in input:
            distances[d.name] += d.step()
    print(max(distances.values()))


def solve2(input) -> None:
    points = {d.name: 0 for d in input}
    distances = {d.name: 0 for d in input}
    for i in range(2503):
        for d in input:
            distances[d.name] += d.step()
        max_distance = max(distances.values())
        for d in input:
            if distances[d.name] == max_distance:
                points[d.name] += 1

    print(max(points.values()))


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(deepcopy(input))
    solve2(deepcopy(input))
