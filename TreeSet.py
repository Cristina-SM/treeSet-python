from Nodo import Node

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value, None)
        else:
            self.root.add(value, None)

    # # def contains(self, value):
    # #     if self.root == None:
    # #         return False
    # #     else:
    # #         return self.root.contains(value)

    # def remove(self, value):
    #     if self.root != None:
    #         self.root = self.root.remove(value)

    def __str__(self):
        if self.root == None:
            return ""
        else:
            return self.root.__str__()
