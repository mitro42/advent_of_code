import math
from itertools import product

import read_input

GEAR = {
    'Dagger': [8, 4, 0],
    'Shortsword': [10, 5, 0],
    'Warhammer': [25, 6, 0],
    'Longsword': [40, 7, 0],
    'Greataxe': [74, 8, 0],
    'Leather': [13, 0, 1],
    'Chainmail': [31, 0, 2],
    'Splintmail': [53, 0, 3],
    'Bandedmail': [75, 0, 4],
    'Platemail': [102, 0, 5],
    'Damage +1': [25, 1, 0],
    'Damage +2': [50, 2, 0],
    'Damage +3': [100, 3, 0],
    'Defense +1': [20, 0, 1],
    'Defense +2': [40, 0, 2],
    'Defense +3': [80, 0, 3],
    'None': [0, 0, 0],
}

WEAPONS = [
    'Dagger',
    'Shortsword',
    'Warhammer',
    'Longsword',
    'Greataxe',
]

ARMORS = [
    'None',
    'Leather',
    'Chainmail',
    'Splintmail',
    'Bandedmail',
    'Platemail',
]

RINGS = [
    'None',
    'Damage +1',
    'Damage +2',
    'Damage +3',
    'Defense +1',
    'Defense +2',
    'Defense +3',
]


class Creature:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def take_damage(self, damage):
        self.hp -= max(1, damage - self.armor)

    def is_dead(self):
        return self.hp <= 0

    def __str__(self):
        return f'{self.name:6}, armor {self.armor}, damage {self.damage}, hp {self.hp}'


class Player(Creature):
    def __init__(self):
        super().__init__('Player', hp=100, damage=0, armor=0)
        self.cost = 0
        self.gear = []

    def add_gear(self, name):
        cost, damage, armor = GEAR[name]
        self.gear.append(name)
        self.cost += cost
        self.damage += damage
        self.armor += armor


class Enemy(Creature):
    def __init__(self, hp, damage, armor):
        super().__init__('Enemy', hp=hp, damage=damage, armor=armor)

    def clone(self):
        return Enemy(hp=self.hp, damage=self.damage, armor=self.armor)


def play(player: Creature, enemy: Creature, dump: bool = True) -> bool:
    if dump:
        print(player)
        print(enemy)
    while True:
        enemy.take_damage(player.damage)
        if enemy.is_dead():
            return True
        player.take_damage(enemy.damage)
        if player.is_dead():
            return False
        if dump:
            print(player)
            print(enemy)
            print('-' * 50)


def parse_input() -> Enemy:
    lines = read_input.strings(sep=' ')
    hp = int(lines[0][2])
    damage = int(lines[1][1])
    armor = int(lines[2][1])

    return Enemy(hp, damage, armor)


def create_player(weapon, armor, ring1, ring2):
    if ring1 == ring2 and ring1 != 'None':
        return None

    p = Player()
    p.add_gear(weapon)
    p.add_gear(armor)
    p.add_gear(ring1)
    p.add_gear(ring2)
    return p


def solve1(enemy) -> None:
    min_cost = math.inf
    min_gear = []
    for items in product(WEAPONS, ARMORS, RINGS, RINGS):
        p = create_player(*items)
        if p is None:
            continue
        win = play(p, enemy.clone(), dump=False)
        if win:
            if p.cost < min_cost:
                min_cost = p.cost
                min_gear = p.gear.copy()
    print(min_cost)
    # print(min_gear)


def solve2(enemy) -> None:
    max_cost = 0
    max_gear = []
    for items in product(WEAPONS, ARMORS, RINGS, RINGS):
        p = create_player(*items)
        if p is None:
            continue
        win = play(p, enemy.clone(), dump=False)
        if not win:
            if p.cost > max_cost:
                max_cost = p.cost
                max_gear = p.gear.copy()
    print(max_cost)
    # print(max_gear)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve1(input)
    solve2(input)
