from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                s.discard(n)
        return next(iter(s))
