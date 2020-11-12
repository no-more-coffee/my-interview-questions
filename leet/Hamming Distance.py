class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(1 if c == '1' else 0 for c in bin(x ^ y))
