from collections import defaultdict, Counter
from functools import lru_cache


@lru_cache
def sum_digits(n):
    return sum(int(i) for i in str(n))


class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = defaultdict(int)
        for i in range(1, n + 1):
            sums[sum_digits(i)] += 1

        return max(Counter(sums.values()).items())[1]


print(Solution().countLargestGroup(13))
print(Solution().countLargestGroup(2))
print(Solution().countLargestGroup(15))
print(Solution().countLargestGroup(24))
