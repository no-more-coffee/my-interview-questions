from functools import lru_cache
from math import sqrt

primes = [2, 3]


@lru_cache
def get_next_prime(primes):
    for i in range(primes[-1], 100000, 2):
        if not (i - 1) % 6 or not (i + 1) % 6:
            for j in primes:
                if not i % j:
                    break
                if j > sqrt(i):
                    return i
            else:
                return i
