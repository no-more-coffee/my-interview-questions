# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level = (root,)
        result = []

        while level:
            level_result = []
            children = deque(())
            for node in level:
                if not node:
                    continue
                level_result.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            level = children
            if level_result:
                result.append(level_result)

        return result
