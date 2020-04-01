from collections import deque


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val},{self.left},{self.right}'


class Codec:
    def serialize(self, root):
        def do(node):
            yield str(node.val)
            yield ','

            if node.left:
                yield '<'
                yield from do(node.left)
                yield '|'

            if node.right:
                yield '>'
                yield from do(node.right)
                yield '|'

        if not root:
            return ''
        return ''.join(do(root))

    def deserialize(self, data):
        if not data:
            return None

        val_syms = ''
        queue = deque((TreeNode(None),))
        for t in data:
            if t == '|':
                queue.pop()
            elif t == '<':
                node = queue[-1]
                node.left = TreeNode(None)
                queue.append(node.left)
            elif t == '>':
                node = queue[-1]
                node.right = TreeNode(None)
                queue.append(node.right)
            elif t == ',':
                node = queue[-1]
                node.val = int(val_syms)
                val_syms = ''
            else:
                val_syms += t

        return queue.pop()


def run(root):
    codec = Codec()
    encoded = codec.serialize(root)
    print(encoded)
    decoded = codec.deserialize(encoded)
    print(root)


run(TreeNode(11, left=TreeNode(22), right=TreeNode(33, left=TreeNode(44), right=TreeNode(55))))
run(TreeNode(11))
run(TreeNode(11, left=TreeNode(22)))
run(TreeNode(-11, left=TreeNode(11), right=TreeNode(22)))
