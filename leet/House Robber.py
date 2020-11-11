from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def rob_i(i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            return max(nums[i] + rob_i(i + 2), nums[i + 1] + rob_i(i + 3))

        return rob_i(0)
