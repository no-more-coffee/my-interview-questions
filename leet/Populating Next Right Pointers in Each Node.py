# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def do(*nodes):
            children = []
            last = None
            for n in nodes:
                if not n:
                    return
                n.next = last
                last = n
                children.append(n.right)
                children.append(n.left)
            do(*children)

        do(root)
        return root
