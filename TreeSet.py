from ClassCastException import ClassCastException
from Nodo import Node
from NullPointerException import NullPointerException
from NoSuchElementException import NoSuchElementException
from Tree_Aux import AVL_tree

class TreeSet(AVL_tree):

    def __init__(self, tree_type):
        self.root = None
        if (tree_type).__eq__ is object.__eq__ or (tree_type).__lt__ is object.__lt__:
            raise ClassCastException(
                "El elemento no es implementa la clase comparable."
            )
        self.tree_type = tree_type
        self.size = 0

    def add(self, key):
        if self.root is None:
            if type(key) is not self.tree_type:
                raise ClassCastException(
                    f"El elemento a introducir no es del tipo {self.tree_type}."
                )
            self.root = Node(key)
            return True
        elif self.root is not None and self.tree_type is not type(key):
            raise ClassCastException(f"El elemento no es del tipo {self.tree_type}.")
        elif key is None:
            raise NullPointerException("El elemento a introducir no puede ser nulo")
        elif self.find(key) is None:
            self._add(key, self.root)
            return True
        return False

    def addAll(self, collection):
        flag = True
        for i in collection:
            if i is None:
                raise NullPointerException("El elemento a introducir no puede ser nulo")
            elif type(i) is not self.tree_type:
                raise ClassCastException(
                    f"El elemento no es del tipo {self.tree_type}."
                )
                
        if flag:
            for i in collection:
                self.add(i)
        return flag

    def ceiling(self, value):
        return self._ceiling_recursive(self.root, value)

    def clear(self):
        self.root = None
        self._size = 0

    def clone(self):
        cloned_tree_set = TreeSet(self.tree_type)
        cloned_tree_set.root = self._clone_recursive(self.root)
        cloned_tree_set.size = self.size

        return cloned_tree_set

    def contains(self, key):
        if key is None:
            raise NullPointerException("No existen elementos nulos en el árbol.\n")
        elif self.tree_type is not type(key):
            raise ClassCastException("No existen elementos de este tipo en el árbol.\n")
        return self._search(key, self.root)

    def descendingIterator(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return reversed(elements)

    def first(self):
        if (self.root is None):
            raise NoSuchElementException("No hay elementos en el árbol")
        return next(iter(self))

    def floor(self, key):
        if key is None:
            raise NullPointerException("No existen elementos nulos en el árbol.\n")
        elif self.tree_type is not type(key):
            raise ClassCastException("No existen elementos de este tipo en el árbol.\n")
        current = self.root
        floor = None
        while current is not None:
            if current.key <= key:
                floor = current.key
                current = current.right
            else:
                current = current.left
        return floor

    def higher(self, key):
        if key is None:
            raise NullPointerException("No existen elementos nulos en el árbol.\n")
        elif self.tree_type is not type(key):
            raise ClassCastException("No existen elementos de este tipo en el árbol.\n")
        current = self.root
        higher = None
        while current is not None:
            if current.key > key:
                higher = current.key
                current = current.left
            else:
                current = current.right
        return higher

    def isEmpty(self):
        return self.root is None

    def iterator(self):
        return self._inorder_generator(self.root)

    def last(self):
        if (self.root is None):
            raise NoSuchElementException("No hay elementos en el árbol")
        return next(self.descendingIterator())

    def lower(self, key):
        if key is None:
            raise NullPointerException("No existen elementos nulos en el árbol.\n")
        elif self.tree_type is not type(key):
            raise ClassCastException("No existen elementos de este tipo en el árbol.\n")
        current = self.root
        lower = None
        while current is not None:
            if current.key < key:
                lower = current.key
                current = current.right
            else:
                current = current.left
        return lower

    def pollFirst(self):
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        self.remove(current.key)
        return current.key

    def pollLast(self):
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right

        self.remove(current.key)
        return current.key

    def remove(self, key):
        return self.remove_node(self.find(key))

    def size(self):
        return self._size_recursive(self.root)

    def __str__(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        if len(elements) == 0:
            return "[]"
        return "['" + "', '".join(map(str, elements)) + "']"

    def __iter__(self):
        return self._inorder_generator(self.root)
