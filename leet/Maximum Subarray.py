from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        it = iter(nums)
        last_max = top = next(it)
        for n in it:
            last_max = n if last_max < 0 else last_max + n
            top = max(top, last_max)
        return top


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        it = iter(nums)
        last_max = top = next(it)
        for n in it:
            last_max = max(last_max + n, n)
            top = max(top, last_max)
        return top


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        summ = max(nums)
        for n in nums:
            if curr + n > 0:
                curr = curr + n
                summ = max(summ, curr)
            else:
                curr = 0
        return summ
