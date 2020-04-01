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
        # actions = {
        #     '|': None,
        #     '<': None,
        #     '>': None,
        # }

        def undo(node, start=0):
            while start < finish:
                if data[start] == '|':
                    return start + 1

                if data[start] == '<':
                    node.left = TreeNode(None)
                    start = undo(node.left, start + 1)
                    continue

                if data[start] == '>':
                    node.right = TreeNode(None)
                    start = undo(node.right, start + 1)
                    continue

                end = start
                while data[end] != ',':
                    end += 1

                val = int(data[start:end])
                node.val = val
                start = end + 1

        if not data:
            return None

        finish = len(data)
        root = TreeNode(None)
        undo(root)
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
