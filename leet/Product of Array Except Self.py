from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def build_L():
            l = 1
            yield l
            for i in range(1, len(nums)):
                l *= nums[i - 1]
                yield l

        res = list(build_L())

        r = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= r
            r *= nums[i]
        return res


print(Solution().productExceptSelf([4, 5, 1, 8, 2]), [80, 16, 16, 2, 1])
print(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
print(Solution().productExceptSelf([1, 0]), [0, 1])
print(Solution().productExceptSelf([0, 0]), [0, 0])
