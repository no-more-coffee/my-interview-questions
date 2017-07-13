from itertools import chain


class Friends:
    def __init__(self, connections):
        self.connections = set(frozenset(x) for x in connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        self.connections.add(frozenset(connection))
        return True

    def remove(self, connection):
        try:
            self.connections.remove(connection)
            return True
        except KeyError:
            return False

    def names(self):
        return set(chain.from_iterable(self.connections))

    def connected(self, name):
        return set(chain.from_iterable((c - {name}) for c in self.connections if name in c))
