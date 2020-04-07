from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            groups.setdefault(''.join(sorted(s)), []).append(s)
        return groups.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
