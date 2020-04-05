from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_i = 0
        max_profit = 0
        for i in range(1, len(prices)):
            min_price_i = i if prices[min_price_i] > prices[i] else min_price_i
            max_profit = max(prices[i] - prices[min_price_i], max_profit)
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)
print(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
