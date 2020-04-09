from itertools import zip_longest


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def iter_str(s):
            backs = 0
            i = len(s)
            while i > 0:
                i -= 1
                if s[i] == '#':
                    backs += 1
                    continue
                if backs:
                    backs -= 1
                    continue
                yield s[i]

        return all(v1 == v2 for v1, v2 in zip_longest(iter_str(S), iter_str(T)))


print(Solution().backspaceCompare(S="ab#c", T="ad#c"))
print(Solution().backspaceCompare(S="ab##", T="c#d#"))
print(Solution().backspaceCompare(S="a##c", T="#a#c"))
print(Solution().backspaceCompare(S="a#c", T="b"))
print(Solution().backspaceCompare(S="bxj##tw", T="bxj###tw"))
