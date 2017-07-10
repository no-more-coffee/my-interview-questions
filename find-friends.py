class Tree:
    def __init__(self, name, links=None):
        self.name = name
        self.links = links if links else ()


def populate_tree(name: str, network: tuple):
    found_links = (n.replace(name, '').replace('-', '') for n in network if name in n)
    other_links = tuple(n for n in network if name not in n)

    links = (populate_tree(l, other_links) for l in found_links)
    return Tree(name, links)


def search_tree(tree: Tree, find_name):
    if tree.name == find_name:
        return True
    for node in tree.links:
        return search_tree(node, find_name)
    return False


def check_connection(network, first, second):
    tree = populate_tree(first, network)
    return search_tree(tree, second)
