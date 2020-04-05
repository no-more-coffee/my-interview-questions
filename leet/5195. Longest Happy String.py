from typing import NamedTuple


class CountChar(NamedTuple):
    count: int
    char: str


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        char_counts = {'a': a, 'b': b, 'c': c}
        last, second, first = sorted((CountChar(count, char) for char, count in char_counts.items()))

        use_n_first = min(2, first.count)
        if second.count == 0:
            return first.char * use_n_first

        use_n_second = int(first.count - use_n_first >= second.count)

        char_counts[first.char] -= use_n_first
        char_counts[second.char] -= use_n_second
        return (first.char * use_n_first) + (second.char * use_n_second) + self.longestDiverseString(**char_counts)


print(Solution().longestDiverseString(a=1, b=1, c=7))
print(Solution().longestDiverseString(a=2, b=2, c=1))
print(Solution().longestDiverseString(a=7, b=1, c=0))
r = Solution().longestDiverseString(0, 8, 11)
print(r, len(r))
