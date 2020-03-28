from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def do(inorder, post_i):
            if not inorder:
                return None

            while postorder[post_i] not in inorder:
                post_i -= 1

            node = TreeNode(postorder[post_i])

            is_left = True
            left_in = []
            right_in = []
            for i in inorder:
                if i == node.val:
                    is_left = False
                    continue

                if is_left:
                    left_in.append(i)
                else:
                    right_in.append(i)

            node.right = do(right_in, post_i - 1)
            node.left = do(left_in, post_i - 1)
            return node

        return do(inorder, -1)


print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
print(Solution().buildTree([2, 1], [2, 1]))
print(Solution().buildTree([2, 3, 1], [3, 2, 1]))
