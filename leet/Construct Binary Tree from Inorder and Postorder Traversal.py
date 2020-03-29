from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def __init__(self) -> None:
        self.post_i = 0

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def do(in_first, in_last):
            if in_first > in_last:
                return None

            current = postorder[self.post_i]
            node = TreeNode(current)
            self.post_i -= 1

            if in_first == in_last:
                return node

            current_i = in_indexes[current]
            node.right = do(current_i + 1, in_last)
            node.left = do(in_first, current_i - 1)
            return node

        self.post_i = len(postorder) - 1
        in_indexes = {v: i for i, v in enumerate(inorder)}
        return do(0, len(inorder) - 1)


print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
print(Solution().buildTree([2, 1], [2, 1]))
print(Solution().buildTree([2, 3, 1], [3, 2, 1]))
