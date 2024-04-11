import functools

class Node:
    @total_ordering
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def __lt__(self, other):
        return self.data < other.data
    def __gt__(self, other):
        return self.data > other.data
    def __eq__(self, other):
        return self.data == other.data