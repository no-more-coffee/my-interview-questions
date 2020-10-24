from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        ptr = 0
        last = None
        for num in nums:
            if num != last:
                l += 1
                nums[ptr] = last = num
                ptr += 1
        # nums = nums[:l]
        return l
