class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1 = sum(range(len(nums) + 1))
        s2 = sum(nums)
        return s1 - s2
