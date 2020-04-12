class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def do(node):
            if not node:
                return 0

            left_children_max = do(node.left)
            right_children_max = do(node.right)
            self.diameter = max(self.diameter, 1 + left_children_max + right_children_max - 1)
            return max(left_children_max, right_children_max) + 1

        self.diameter = 0
        do(root)
        return self.diameter
