class Solution:
    def reverse(self, x: int) -> int:
        digits = int(str(abs(x))[::-1])
        result = -digits if x < 0 else digits
        if -2 ** 31 < result < 2 ** 31 - 1:
            return result
        return 0


print(123, Solution().reverse(123))
print(-123, Solution().reverse(-123))
