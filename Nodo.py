from functools import total_ordering

class Node:
    def __init__(self, key, node):
        self.key = key
        self.parent = node
        self.right = None
        self.left = None
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
    