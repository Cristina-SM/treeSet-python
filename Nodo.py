from functools import total_ordering

class Node:
    def __init__(self, key, Node):
        self.key = key
        self.parent = Node
        self.right = None
        self.left = None
<<<<<<< HEAD
    def __lt__(self, other):
        return self.key < other.key
=======

>>>>>>> b22e5e345f16b9cb7b5bc4d2428dda232a331932
    def __gt__(self, other):
        return self.key > other.key
    def __eq__(self, other):
        if other == None:
            return False
        return self.key == other.key
    def __str__(self):
        return f"{self.key}"
    