class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s) // 2 + 1):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


print(121, Solution().isPalindrome(121))
