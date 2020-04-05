from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        rev = sorted(nums)
        rev.reverse()
        for i in range(1, len(nums)):
            if sum(rev[:i]) > sum(rev[i:]):
                return rev[:i]
        return rev


print(Solution().minSubsequence([3, 5]))
