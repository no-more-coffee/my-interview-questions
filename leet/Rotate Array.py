class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        cur = start = 0
        k = k % len(nums)
        buf = nums[0]

        for _ in range(len(nums)):
            buf, nums[(cur + k) % len(nums)] = nums[(cur + k) % len(nums)], buf
            if (cur + k) % len(nums) == start:
                cur = start = (start + 1) % len(nums)
                buf = nums[cur]
            else:
                cur = (cur + k) % len(nums)
