class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


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
        def undo(d, node):
            while d:
                if d[0] == '|':
                    return d[1:]

                if d[0] == '<':
                    node.left = TreeNode(None)
                    d = undo(d[1:], node.left)
                    continue

                if d[0] == '>':
                    node.right = TreeNode(None)
                    d = undo(d[1:], node.right)
                    continue

                end = d.index(',')
                val = eval(d[:end])
                node.val = val
                d = d[end + 1:]

        if not data:
            return None

        root = TreeNode(None)
        undo(data, root)
        return root


def run(root):
    codec = Codec()
    encoded = codec.serialize(root)
    print(encoded)
    decoded = codec.deserialize(encoded)
    print(root == decoded)


run(TreeNode(11, left=TreeNode(22), right=TreeNode(33, left=TreeNode(44), right=TreeNode(55))))
run(TreeNode(11))
run(TreeNode(11, left=TreeNode(22)))
