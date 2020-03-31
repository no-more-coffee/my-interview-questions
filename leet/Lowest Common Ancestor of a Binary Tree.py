# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def do(self, node: TreeNode, found_p=False, found_q=False):
        came_with_nothing = not (found_p or found_q)
        if not node:
            return found_p, found_q
        found_p = found_p or node == self.p
        found_q = found_q or node == self.q

        if found_p and found_q:
            return found_p, found_q

        res_left_p, res_left_q = self.do(node.left, found_p, found_q)
        if res_left_p and res_left_q:
            if came_with_nothing:
                self.lcas.append(node)
            return True, True
        else:
            found_p = found_p or res_left_p
            found_q = found_q or res_left_q

        res_right_p, res_right_q = self.do(node.right, found_p, found_q)
        if res_right_p and res_right_q:
            if came_with_nothing:
                self.lcas.append(node)
            return True, True
        else:
            found_p = found_p or res_right_p
            found_q = found_q or res_right_q

        return found_p, found_q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lcas = deque(())
        self.p = p
        self.q = q
        self.do(root)
        return self.lcas.popleft()
