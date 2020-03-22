from typing import List


def sumFour(num):
    s = 0
    count = 0
    i = 1
    while i * i <= num:
        q, r = divmod(num, i)
        if r:
            i += 1
            continue
        count += 1
        s += i
        if i * i < num:
            count += 1
            s += q
        i += 1
        if count > 4:
            return 0
    return s if count == 4 else 0


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(sumFour(n) for n in nums)


print(Solution().sumFourDivisors(nums=[21, 4, 7]))
print(Solution().sumFourDivisors(nums=[1, 2, 3, 4, 5]))
print(Solution().sumFourDivisors(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
