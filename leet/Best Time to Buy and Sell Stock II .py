from functools import lru_cache
from typing import List


@lru_cache
def max_p(*prices):
    result = 0
    first_small = 0
    for i in range(1, len(prices)):
        if prices[i] <= prices[first_small]:
            first_small += 1
            continue
        m = max(
            (prices[l] - prices[first_small] + max_p(*prices[l + 1:]))
            for l in range(i, len(prices))
            if prices[l] > prices[first_small]
        )
        result = max(m, result)
    return result


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max_p(*prices)


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
