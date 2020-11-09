from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        last = prices[0]
        maxdiff = 0
        lowest = float('inf')

        for p in prices[1:]:
            if p <= last:
                last = p
                continue
            maxdiff = max(maxdiff, p - last, p - lowest)
            lowest = min(last, lowest)
            last = p

        return maxdiff
