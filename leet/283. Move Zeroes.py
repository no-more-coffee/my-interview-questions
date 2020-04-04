from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero = None
        for i in range(len(nums)):
            if nums[i]:
                if first_zero is not None:
                    nums[first_zero], nums[i] = nums[i], 0
                    first_zero += 1
                continue
            if first_zero is None:
                first_zero = i
