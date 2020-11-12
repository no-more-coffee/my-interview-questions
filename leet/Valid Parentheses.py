from collections import deque

REVERSES = {
    ')': '(',
    ']': '[',
    '}': '{',
}

class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()
        for c in s:
            if c in '({[':
                queue.append(c)
            else:
                if REVERSES.get(c) != queue.pop():
                    return False

        return not queue
