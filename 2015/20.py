from functools import cache

from primes import PrimeStore

ps = PrimeStore()


@cache
def s(p, power):
    return (sum([p**i for i in range(power + 1)]))


@cache
def get_house_gifts(house):
    if house == 1:
        return 1
    if ps.is_prime_fast(house):
        return house + 1
    else:
        p, pow = ps.smallest_factor_with_power(house)
        gifts = get_house_gifts(house // (p**pow)) * s(p, pow)
        return gifts


def solve1(input) -> None:
    n = 1
    max_gifts = 0
    while True:
        gifts = get_house_gifts(n)

        # if n % 10000 == 0:
        #     print(n)
        if gifts > max_gifts:
            max_gifts = gifts
            # print(n, max_gifts)
        if input < gifts:
            print(n)
            return
        n += 1


if __name__ == '__main__':
    input = 34000000
    solve1(input // 10)
    # solve2(input)