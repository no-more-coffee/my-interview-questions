class Solution:
    def numSteps(self, s: str) -> int:
        i = int(s, 2)
        steps = 0
        while i != 1:
            steps += 1
            quotient, remainder = divmod(i, 2)
            if remainder:
                i += 1
            else:
                i = quotient
        return steps


print(Solution().numSteps("1101"))
