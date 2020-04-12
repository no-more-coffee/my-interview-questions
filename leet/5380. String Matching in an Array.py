from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        print(words)
        result = set()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    result.add(words[i])
        return list(result)


print(Solution().stringMatching(words=["mass", "as", "hero", "superhero"]))
print(Solution().stringMatching(words=["leetcode", "et", "code"]))
print(Solution().stringMatching(words=["blue", "green", "bu"]))
print(Solution().stringMatching(words=["leetcoder", "leetcode", "od", "hamlet", "am"]))
