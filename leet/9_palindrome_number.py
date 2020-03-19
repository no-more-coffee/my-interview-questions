def get_reversed_int(x: int):
    return sum(multiply_reversed(iter_digits(x)))


def iter_digits(x: int):
    while x:
        quotient, remainder = divmod(x, 10)
        x = quotient
        yield remainder


def multiply_reversed(digits: iter):
    array = list(digits)
    for i, e in enumerate(array):
        yield e * 10 ** (len(array) - 1 - i)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == get_reversed_int(x)


print(121, Solution().isPalindrome(121))
print(123, Solution().isPalindrome(123))
