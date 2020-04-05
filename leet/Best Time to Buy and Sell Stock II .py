from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        groups = []
        current_group_min_i = 0
        current_group_max_i = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                current_group_max_i = i
            elif prices[i] < prices[i - 1]:
                groups.append((current_group_min_i, current_group_max_i))
                current_group_min_i = i
                current_group_max_i = i
                continue
            if i == len(prices) - 1:
                groups.append((current_group_min_i, current_group_max_i))
        return sum(prices[y] - prices[x] for x, y in groups)


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 7)
print(Solution().maxProfit([1, 2, 3, 4, 5]), 4)
print(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
print(Solution().maxProfit([1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9]), 25)
