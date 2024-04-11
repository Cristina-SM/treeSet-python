from Nodo import Node

class TreeSet:
    def __init__(self):
        self.root = None
        self.lista = []

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
            self.lista.append(value)
        else:
            if value > self.root.key:
                self.root.right = Node(value, self.root)
                self.lista.append(value)

            elif value < self.root.key:
                self.root.left = Node(value, self.root)
                self.lista.append(value)

    # def contains(self, value):
    #     if self.root == None:
    #         return False
    #     else:
    #         return self.root.contains(value)

    def remove(self, value):
        if self.root is None:
            return False
        else:
            while self.root.left is not None or self.root.right is not None:
                if value < self.root.right.key:
                    if value == self.root.key:
                        print("H")
                        self.root.remove(self.root)
                        self.lista.remove(value)
                        return True
                    self.root = self.root.right
                elif value > self.root.left.key:
                    self.root = self.root.left
                    if value == self.root.key:
                        self.root.remove(self.root)
                        self.lista.remove(value)
                        return True

    def __str__(self):
        if self.root == None:
            return ""
        else:
            return f"{sorted(self.lista)}"