from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_children(it):
    res = []
    for i in it:
        if not i:
            continue
        if i.left:
            res.append(i.left)
        if i.right:
            res.append(i.right)
    return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            result.append([v.val for v in queue])
            queue = get_children(queue)
        return result
