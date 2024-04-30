from Nodo import Node


class TreeSet:
    def __init__(self):
        self.root = None
        self.padreTotal = None

    def add(self, value, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(value)
                return
            else:
                node = self.root

        if value < node.key:
            if node.left is None:
                node.left = Node(value)
            else:
                self.add(value, node.left)
        elif value > node.key:
            if node.right is None:
                node.right = Node(value)
            else:
                self.add(value, node.right)

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
                                return True
                            if self.root.left is None:
                                switcher = False
                        elif switcher is True:
                            self.root = self.root.right
                            if value == self.root.key:
                                self.root.remove(self.root)
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
                                return True
                            if self.root.right is None:
                                switcher = False
                        elif switcher is True:
                            self.root = self.root.left
                            if value == self.root.key:
                                self.root.remove(self.root)
                                return True
                            if self.root.left is None:
                                switcher = False
                        else:
                            break
                elif value == self.root.key:
                    temp = self.root.right
                    self.root.remove(self.root)
                    self.root = temp
                    return True
                # aqui falta baaastante codigo todavia, es un simple esquema de como se podria hacer

    
    def size(self):
        return 
    
    def contains(self, value):
        if self.root == None:
            return False
        else:
            while self.root is not None:
                if value < self.root.key:
                    while self.root.left is not None:
                        self.root = self.root.left
                        if value == self.root.key:
                            return True
                        if self.root.left is None:
                            return False
                elif value > self.root.key:
                    while self.root.right is not None:
                        self.root = self.root.right
                        if value == self.root.key:
                            return True
                        if self.root.right is None:
                            return False
                elif value == self.root.key:
                    return True

    def __str__(self):
        if self.root == None:
            return ""
        else:
            return f"{sorted(self.lista)}"
        
   
    def __iter__(self):
        return self.lista.__iter__()
    def __next__(self):
        return self.lista.__next__()
    

    def dfs_descending(self, node=None):
        if node is None:
            node = self.root
        stack = [node]
        while stack:
            node = stack.pop()
            if node is not None:
                yield node.key
                stack.append(node.left)  # Primero se añade el hijo izquierdo al stack
                stack.append(node.right)  # Luego se añade el hijo derecho