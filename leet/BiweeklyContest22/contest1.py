from functools import lru_cache


@lru_cache
def get_power(x, i=1):
    q, r = divmod(x, 2)
    result = 3 * x + 1 if r else q
    if result > 1:
        return get_power(result, i + 1)
    else:
        return i


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        k_ = sorted((get_power(x), x) for x in range(lo, hi + 1))
        return k_[k-1][1]


print(Solution().getKth(lo=12, hi=15, k=2))
print(Solution().getKth(lo=1, hi=1, k=1))
print(Solution().getKth(lo=7, hi=11, k=4))
print(Solution().getKth(lo=10, hi=20, k=5))
print(Solution().getKth(lo=1, hi=1000, k=777))
