class Solution:
    def reverseBits(self, n: int) -> int:
        return int(''.join(reversed(bin(n).replace('0b', '').zfill(32))), 2)
