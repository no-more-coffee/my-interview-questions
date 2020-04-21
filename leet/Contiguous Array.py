from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        v = 0
        m = {0: -1}
        for i in range(len(nums)):
            v = v + 1 if nums[i] else v - 1
            if v in m:
                max_len = max(max_len, i - m[v])
            else:
                m[v] = i
        return max_len


print(Solution().findMaxLength([0, 1]), 2)
print(Solution().findMaxLength([0, 1, 0]), 2)
print(Solution().findMaxLength([0, 0, 1, 1, 1, 0, 0]), 6)
