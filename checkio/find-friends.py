class Tree:
    def __init__(self, name, links=None):
        self.name = name
        self.links = links if links else ()


def populate_tree(name: str, network: tuple):
    other_links = tuple(n for n in network if name not in n)
    found_links = (n.replace(name, '').replace('-', '') for n in network if name in n)

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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
