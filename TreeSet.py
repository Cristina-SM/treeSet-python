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
        switcher = False
        if self.root is None:
            return False
        else:
            while self.root is not None:
                if value < self.root.key:
                    while self.root.left is not None:
                        if switcher is not True:
                            self.root = self.root.left
                            if value == self.root.key:
                                self.root.remove(self.root)
                                self.lista.remove(value)
                                return True
                            if self.root.left is None:
                                switcher = False
                        elif switcher is True:
                            self.root = self.root.right
                            if value == self.root.key:
                                self.root.remove(self.root)
                                self.lista.remove(value)
                                return True
                            if self.root.right is None:
                                switcher = False
                        else:
                            break
                elif value > self.root.key:
                    while self.root.right is not None:
                        if switcher is not True:
                            self.root = self.root.right
                            if value == self.root.key:
                                self.root.remove(self.root)
                                self.lista.remove(value)
                                return True
                            if self.root.right is None:
                                switcher = False
                        elif switcher is True:
                            self.root = self.root.left
                            if value == self.root.key:
                                self.root.remove(self.root)
                                self.lista.remove(value)
                                return True
                            if self.root.left is None:
                                switcher = False
                        else:
                            break
                elif value == self.root.key:
                    temp = self.root.right
                    self.root.remove(self.root)
                    self.lista.remove(value)
                    self.root = temp
                    return True
                # aqui falta baaastante codigo todavia, es un simple esquema de como se podria hacer

    def __str__(self):
        if self.root == None:
            return ""
        else:
            return f"{sorted(self.lista)}"