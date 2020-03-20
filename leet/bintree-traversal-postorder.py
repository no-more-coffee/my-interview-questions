# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack1 = deque((root,))
        stack2 = deque(())

        while stack1:
            node = stack1.pop()
            if not node:
                continue
            stack2.appendleft(node.val)
            stack1.append(node.left)
            stack1.append(node.right)

        return list(stack2)
