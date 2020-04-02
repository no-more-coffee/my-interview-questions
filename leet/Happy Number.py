from functools import lru_cache


@lru_cache
def pow_2(c) -> int:
    return int(c) ** 2


class Solution:
    def isHappy(self, n: int) -> bool:
        spotted = set()
        while n != 1:
            n = sum(pow_2(c) for c in str(n))
            if n in spotted:
                return False
            spotted.add(n)
        return True


print(Solution().isHappy(19))
