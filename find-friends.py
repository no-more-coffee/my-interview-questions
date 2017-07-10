class Tree:
    def __init__(self, name, links=None):
        self.name = name
        self.links = links if links else []

    def __str__(self):
        return str(self.name)


def populate_tree(name: str, network: tuple):
    found_links = tuple(filter(lambda x: name in x, network))
    other_links = tuple(x for x in network if x not in found_links)

    links = []
    for link in found_links:
        node = link.replace(name, '').replace('-', '')
        links.append(populate_tree(node, other_links))
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
