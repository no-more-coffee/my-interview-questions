from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(
            max(0, prices[i] - prices[i - 1])
            for i in range(1, len(prices))
        )


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 7)
print(Solution().maxProfit([1, 2, 3, 4, 5]), 4)
print(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
print(Solution().maxProfit([1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9]), 25)
