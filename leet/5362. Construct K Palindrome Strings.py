from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        return sum(c % 2 for c in Counter(s).values()) <= k


print(Solution().canConstruct(s="annabelle", k=2))
print(Solution().canConstruct(s="leetcode", k=3))
print(Solution().canConstruct(s="true", k=4))
print(Solution().canConstruct(s="yzyzyzyzyzyzyzy", k=2))
print(Solution().canConstruct(s="cr", k=7))
