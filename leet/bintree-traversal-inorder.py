# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def yieldValues(node: TreeNode):
    stack = deque(())

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        yield node.val
        node = node.right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return list(yieldValues(root))
