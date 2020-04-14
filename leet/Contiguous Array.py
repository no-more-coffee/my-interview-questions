from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        temp = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                temp[i] -= 1
            else:
                temp[i] += 1
            if temp[i] == 0:
                max_len = max(max_len, )
        return max_len


print(Solution().findMaxLength([0, 1]), 2)
print(Solution().findMaxLength([0, 1, 0]), 2)
print(Solution().findMaxLength([0, 0, 1, 1, 1, 0, 0]), 2)
