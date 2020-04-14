from collections import deque
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        queue = deque(s)
        for d, n in shift:
            n = n if d else -1 * n
            queue.rotate(n)
        return ''.join(queue)


print(Solution().stringShift(s="abc", shift=[[0, 1], [1, 2]]), 'cab')
print(Solution().stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]]), 'efgabcd')
print(Solution().stringShift(s="mecsk", shift=[[1, 4], [0, 5], [0, 4], [1, 1], [1, 5]]), "kmecs")
