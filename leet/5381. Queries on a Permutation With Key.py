from collections import deque
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = deque(range(1, m + 1))
        res = []
        for q in queries:
            i = P.index(q)
            res.append(i)
            P.remove(q)
            P.appendleft(q)
        return res


print(Solution().processQueries(queries=[3, 1, 2, 1], m=5), [2, 1, 2, 1])
print(Solution().processQueries(queries=[4, 1, 2, 2], m=4), [3, 1, 2, 0])
print(Solution().processQueries(queries=[7, 5, 5, 8, 3], m=8), [6, 5, 0, 7, 5])
