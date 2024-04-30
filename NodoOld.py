
class Node:
    def __init__(self, key, node):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None
        self.height = 1

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        if other == None:
            return False
        return self.key == other.key

    def remove(self, node):
        node.key == None
        node.parent = None
        node.right = None
        node.left = None

    def __str__(self):
        return f"{self.key}"
