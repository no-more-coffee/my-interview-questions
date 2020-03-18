class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = -x if is_negative else x
        result = int(str(x)[::-1])
        result = -result if is_negative else result
        if -2 ** 31 > result or result > 2 ** 31 - 1:
            return 0
        return result


print(123, Solution().reverse(123))
print(-123, Solution().reverse(-123))
