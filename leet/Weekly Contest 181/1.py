from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        a = []
        for i, n in zip(index, nums):
            print(i, n)
            a.insert(i, n)
        return a


print(Solution().createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
print(Solution().createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
print(Solution().createTargetArray(nums = [1], index = [0]))
