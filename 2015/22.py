from __future__ import annotations
import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Tuple

import read_input


@dataclass
class Effect:
    name: str
    remaining: int


class Spell(Enum):
    magic_missile = 0
    drain = 1
    shield = 2
    poison = 3
    recharge = 4


class Creature:
    def __init__(self, name, hp, damage):
        self.name = name
        self.armor = 0
        self.max_hp = hp
        self.hp = hp
        self.damage = damage

    def take_damage(self, damage):
        self.hp -= max(1, damage - self.armor)

    def is_dead(self):
        return self.hp <= 0


class Player(Creature):
    def __init__(self, hp=50, mana=500, armor=0):
        super().__init__('Player', hp=hp, damage=0)
        self.mana = mana
        self.armor = armor

    def __str__(self):
        return f'{self.name}, hp {self.hp}, armor {self.armor}, mana {self.mana}'

    def clone(self):
        return Player(hp=self.hp, mana=self.mana, armor=self.armor)


class Enemy(Creature):
    def __init__(self, hp, damage):
        super().__init__('Enemy', hp=hp, damage=damage)

    def __str__(self):
        return f'{self.name}, hp {self.hp}, damage {self.damage}'

    def clone(self):
        return Enemy(hp=self.hp, damage=self.damage)


COSTS: Dict[Spell, int] = {
    Spell.magic_missile: 53,
    Spell.drain: 73,
    Spell.shield: 113,
    Spell.poison: 173,
    Spell.recharge: 229,
}


@dataclass
class GameState:
    player: Player
    enemy: Enemy
    effects: Dict[Spell, int] = field(default_factory=dict)
    turn: int = 0
    mana_spent: int = 0

    def win(self) -> bool:
        return self.enemy.is_dead()

    def lose(self) -> bool:
        return self.player.is_dead()

    def finished(self) -> bool:
        return self.win() or self.lose()

    def is_valid(self, spell: Spell) -> bool:
        if COSTS[spell] > self.player.mana:
            return False

        if self.effects.get(spell, 0) > 0:
            return False

        return True

    def apply_effects(self):
        if Spell.poison in self.effects:
            self.enemy.hp -= 3
        if Spell.recharge in self.effects:
            self.player.mana += 101

    def expire_effects(self):
        to_delete = []
        for s in self.effects:
            self.effects[s] -= 1
            if self.effects[s] < 0:
                if s == Spell.shield:
                    self.player.armor = 0
                to_delete.append(s)

        for s in to_delete:
            del self.effects[s]

    def enemy_attack(self):
        self.player.take_damage(self.enemy.damage)

    def player_cast(self, spell: Spell):
        self.player.mana -= COSTS[spell]
        self.mana_spent += COSTS[spell]
        if spell == Spell.magic_missile:
            self.enemy.hp -= 4
        elif spell == Spell.drain:
            self.player.hp += 2
            self.enemy.hp -= 2
        elif spell == Spell.shield:
            self.player.armor = 7
            self.effects[spell] = 6
        elif spell == Spell.poison:
            self.effects[spell] = 6
        elif spell == Spell.recharge:
            self.effects[spell] = 5

    def step(self, spell: Spell, hard_mode: bool) -> GameState:
        ns = GameState(player=self.player.clone(),
                       enemy=self.enemy.clone(),
                       effects=self.effects.copy(),
                       turn=self.turn + 2,
                       mana_spent=self.mana_spent)

        if hard_mode:
            if not ns.finished():
                ns.player.take_damage(1)

        if not ns.finished():
            ns.apply_effects()

        if not ns.finished():
            ns.player_cast(spell)

        ns.expire_effects()

        if not ns.finished():
            ns.apply_effects()

        if not ns.finished():
            ns.enemy_attack()

        ns.expire_effects()
        return ns


def play():
    # p = Player(hp=10, mana=250)
    # e = Enemy(hp=13, damage=8)
    # spells = [Spell.poison, Spell.magic_missile]
    p = Player(hp=10, mana=250)
    e = Enemy(hp=14, damage=8)
    spells = [
        Spell.recharge, Spell.shield, Spell.drain, Spell.poison,
        Spell.magic_missile
    ]
    gs = GameState(player=p, enemy=e)
    print('START')
    print(gs.player)
    print(gs.enemy)
    print()

    for s in spells:
        gs = gs.step(s)
        print(gs.turn)
        print(gs.player)
        print(gs.enemy)
        print(gs.effects)
        print()
    if gs.win():
        print('VICTORY')
    if gs.lose():
        print('DEFEAT')


def parse_input() -> Enemy:
    lines = read_input.strings(sep=' ')
    hp = int(lines[0][2])
    damage = int(lines[1][1])

    return Enemy(hp, damage)


def solve(enemy: Enemy, hard_mode: bool = False) -> None:
    min_mana = math.inf
    cp: List[Tuple[GameState, int]] = []
    gs = GameState(player=Player(), enemy=enemy)

    cp.append((gs, -1))
    while cp:
        gs, idx = cp.pop()
        if gs.mana_spent > min_mana:
            continue
        if gs.win():
            if min_mana > gs.mana_spent:
                min_mana = gs.mana_spent
            continue
        if gs.lose():
            continue

        if idx == len(Spell) - 1:
            continue

        s = Spell(idx + 1)
        if not gs.is_valid(s):
            cp.append((gs, idx + 1))
            continue

        ngs = gs.step(s, hard_mode)

        cp.append((gs, idx + 1))
        cp.append((ngs, -1))

    print(min_mana)


if __name__ == '__main__':
    input = parse_input()
    # print(input)
    solve(input)
    solve(input, hard_mode=True)
