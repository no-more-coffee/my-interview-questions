from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        it = iter(nums)
        last_max = top = next(it)
        for n in it:
            last_max = n if last_max < 0 else last_max + n
            top = max(top, last_max)
        return top


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        it = iter(nums)
        last_max = top = next(it)
        for n in it:
            last_max = max(last_max + n, n)
            top = max(top, last_max)
        return top
