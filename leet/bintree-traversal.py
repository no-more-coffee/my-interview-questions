# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def yieldValues(node: TreeNode):
    stack = deque((node,))

    while stack:
        node = stack.pop()
        if not node:
            continue

        yield node.val
        stack.append(node.right)
        stack.append(node.left)


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return list(yieldValues(root))
