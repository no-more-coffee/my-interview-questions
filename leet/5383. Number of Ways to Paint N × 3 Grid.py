from functools import lru_cache

R = 1
Y = 2
G = 0


@lru_cache
def do_i(i):
    if i == 1:
        return 3
    return do_i(i - 1) * 2


class Solution:
    def numOfWays(self, n: int) -> int:
        res = 12
        for i in range(2, n + 1):
            res += 10
        return res


print(Solution().numOfWays(n=1), 12)
print(Solution().numOfWays(n=2), 54)
# print(Solution().numOfWays(n=3), 246)
# print(Solution().numOfWays(n=7), 106494)
# print(Solution().numOfWays(n = 5000), 30228214)
