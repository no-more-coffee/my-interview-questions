class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return do(root)


def do(*nodes):
    children = []
    for n in nodes:
        if not n:
            continue
        children.append(n.left)
        children.append(n.right)
    if not children:
        return True
    values = [n and n.val for n in children]
    if values != values[::-1]:
        return False

    return do(*children)
