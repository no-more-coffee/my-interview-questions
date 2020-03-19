# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def yieldValues(node: TreeNode):
    if not node:
        return

    yield node.val
    yield from yieldValues(node.left)
    yield from yieldValues(node.right)


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return list(yieldValues(root))
