import math
import bisect
from functools import cache
from typing import List, Tuple


class PrimeStore:
    def __init__(self, n: int = -1) -> None:
        self._p = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
            281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
            367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
            443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
            523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
            613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
            691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
            787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
            877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
            971, 977, 983, 991, 997
        ]
        self._factors = {}
        if n != -1:
            self.calculate_primes(n)

    def is_known_prime(self, num: int) -> bool:
        if (num == 1) or (num % 2 == 0 and num != 2) or (
                num % 3 == 0 and num != 3) or (num % 5 == 0
                                               and num != 5) or (num % 7 == 0
                                                                 and num != 7):
            return False

        idx = bisect.bisect_left(self._p, num)
        return idx != len(self._p) and self._p[idx] == num

    def calculate_primes(self, up_to: int) -> None:
        for i in range(self._p[-1] + 1, up_to + 1):
            k = 0
            root = int(math.sqrt(i))
            maybePrime = True

            while maybePrime and k < len(self._p) and self._p[k] <= root:
                if i % self._p[k] == 0:
                    maybePrime = False

                k += 1

            if maybePrime:
                self._p.append(i)

    def is_prime(self, num: int) -> bool:
        if num == 0 or num == 1:
            return False

        if num > self._p[-1]:
            self.calculate_primes(num)
            return self._p[-1] == num
        else:
            return self.is_known_prime(num)

    def is_prime_fast(self, num: int) -> bool:
        if num == 0 or num == 1:
            return False

        idx = 1
        while self.nth_prime(idx)**2 <= num:
            if num % self._p[idx - 1] == 0:
                return False
            idx += 1
        return True

    def nth_known_prime(self, n: int) -> int:
        if n <= len(self._p):
            return self._p[n - 1]

        raise ValueError(f'The {n}th prime is not yet known')

    def nth_prime(self, n: int) -> int:
        while len(self._p) < n:
            self.calculate_primes(int(self._p[-1] * 1.3))

        return self._p[n - 1]

    def factors(self, n) -> List[Tuple[int, int]]:
        if n in self._factors:
            return self._factors[n].copy()
        ret = []
        orig_n = n
        idx = 1
        while n != 1:
            p = self.nth_prime(idx)
            power = 0
            while n > 1 and n % p == 0:
                n /= p
                power += 1
            if power > 0:
                ret.append((p, power))
            idx += 1

        self._factors[orig_n] = ret
        return self._factors[orig_n].copy()

    def smallest_factor(self, n) -> int:
        idx = 1
        while n != 1:
            p = self.nth_prime(idx)
            if n % p == 0:
                return p
            idx += 1

    def smallest_factor_with_power(self, n) -> Tuple[int, int]:
        idx = 1
        pow = 0
        while n != 1:
            p = self.nth_prime(idx)
            if n % p == 0:
                while n % p == 0:
                    pow += 1
                    n //= p
                return p, pow
            idx += 1
