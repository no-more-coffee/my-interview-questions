from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = reduce(lambda x, y: x * y, (i for i in nums if i), 1) if any(nums) else 0
        return [round(all_product / i) if i else all_product for i in nums]


print(Solution().productExceptSelf([1, 0]), [0, 1])
print(Solution().productExceptSelf([0, 0]), [0, 0])
print(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
