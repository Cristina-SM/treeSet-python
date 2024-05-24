from ClassCastException import ClassCastException
from Node import Node
from NoSuchElementException import NoSuchElementException
from NullPointerException import NullPointerException
from Tree_Aux import AVL_tree


class TreeSet(AVL_tree):

    class TreeSet:
        def __init__(self, tree_type):
            """
            Initializes a TreeSet object.

            Args:
                tree_type: The type of elements that the TreeSet will store.

            Raises:
                ClassCastException: If the element does not implement the comparable class.
            """
            self.root = None
            if (tree_type).__eq__ is object.__eq__ or (
                tree_type
            ).__lt__ is object.__lt__:
                raise ClassCastException(
                    "The element does not implement the comparable class."
                )
            self.tree_type = tree_type

    def __str__(self):
        """Returns a string representation of the TreeSet in order.

        Returns:
            str: A string representation of the TreeSet in order.
        """
        elements = []
        self._inorder_traversal(self.root, elements)
        if len(elements) == 0:
            return "[]"
        return "['" + "', '".join(map(str, elements)) + "']"

    def __iter__(self):
        """
        Returns an iterator that traverses the elements of the TreeSet in ascending order.
        """
        return self._inorder_generator(self.root)

    def add(self, key):
        """
        Adds a new node with the given key to the TreeSet.

        Args:
            key: The key of the node to be added.

        Returns:
            bool: True if the node is successfully added, False otherwise.

        Raises:
            NullPointerException: If the key is None.
            ClassCastException: If the type of the node to add is not valid.

        """
        if key is None:
            raise NullPointerException("Node to add cannot be None")
        elif self.root is None:
            if type(key) is not self.tree_type:
                raise ClassCastException(
                    f"The type of the node to add is not valid {self.tree_type}."
                )
            self.root = Node(key)
            return True
        elif self.root is not None and self.tree_type is not type(key):
            raise ClassCastException(
                f"The type of the node to add is not valid {self.tree_type}."
            )
        elif self.find(key) is None:
            self._add(key, self.root)
            return True
        return False

    def addAll(self, collection):
        """
        Adds all the elements from the given collection to the TreeSet.

        Args:
            collection: A collection of elements to be added.

        Raises:
            NullPointerException: If the node to addAll is None.
            ClassCastException: If the type of the node is not valid.

        Returns:
            bool: True if at least one element was added, False otherwise.
        """
        flag = False
        for i in collection:
            if i is None:
                raise NullPointerException("Node to addAll cannot be None")
            elif type(i) is not self.tree_type:
                raise ClassCastException(
                    f"The type of the node is not valid {self.tree_type}."
                )
        for i in collection:
            if i is not None and self.find(i) is None:
                flag = True
                self.add(i)
        return flag

    def ceiling(self, value):
        """
        Returns the smallest element in the set that is greater than or equal to the given value.

        Args:
            value: The value to find the ceiling for.

        Returns:
            The smallest element in the set that is greater than or equal to the given value, or None if no such element exists.
        """
        return self._ceiling_recursive(self.root, value)

    def contains(self, key):
        """
        Checks if the TreeSet contains the specified key.

        Args:
            key: The key to be checked.

        Raises:
            NullPointerException: If the key is None.
            ClassCastException: If the type of the key is not valid.

        Returns:
            True if the TreeSet contains the key, False otherwise.
        """
        if key is None:
            raise NullPointerException("Node cannot be None")
        elif self.tree_type is not type(key):
            raise ClassCastException(
                f"The type of the node is not valid {self.tree_type}."
            )
        return self._search(key, self.root)

    def clear(self):
        """
        Clears all elements from the TreeSet.
        """
        self.root = None
        self._size = 0

    def clone(self):
        """
        Creates a deep copy of the TreeSet object.

        Returns:
            A new TreeSet object that is a clone of the original TreeSet.
        """
        cloned_tree_set = TreeSet(self.tree_type)
        # Llamar a una función auxiliar para clonar el árbol
        cloned_tree_set.root = self._clone_recursive(self.root)
        cloned_tree_set._size = self.size()

        return cloned_tree_set

    def descendingIterator(self):
        """
        Returns an iterator that traverses the elements of the TreeSet in descending order.

        Returns:
            iterator: An iterator that traverses the elements of the TreeSet in descending order.
        """
        elements = []
        self._inorder_traversal(self.root, elements)
        return reversed(elements)

    def first(self):
        """
        Returns the first element in the tree.

        Raises:
            NoSuchElementException: If there are no elements in the tree.

        Returns:
            The first element in the tree.
        """
        if self.root is None:
            raise NoSuchElementException("There are no elements in the tree.")
        return next(iter(self))

    def floor(self, key):
        """
        Returns the largest element in the set less than or equal to the given key.

        Args:
            key: The key to compare against.

        Returns:
            The largest element in the set less than or equal to the given key, or None if no such element exists.

        Raises:
            NullPointerException: If the key is None.
            ClassCastException: If the type of the key is not valid for the set.
        """
        if key is None:
            raise NullPointerException("Node cannot be None.")
        elif self.tree_type is not type(key):
            raise ClassCastException(
                f"The type of the node is not valid {self.tree_type}."
            )
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
        """
        Returns the smallest element in the set that is strictly greater than the given key.

        Args:
            key: The key to compare against.

        Returns:
            The smallest element in the set that is strictly greater than the given key.

        Raises:
            NullPointerException: If the key is None.
            ClassCastException: If the type of the key is not valid for the set.
        """
        if key is None:
            raise NullPointerException("Node cannot be None.")
        elif self.tree_type is not type(key):
            raise ClassCastException(
                f"The type of the node is not valid {self.tree_type}."
            )
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
        """
        Checks if the TreeSet is empty.

        Returns:
            bool: True if the TreeSet is empty, False otherwise.
        """
        return self.root is None

    def last(self):
        """
        Returns the last element in the tree.

        Raises:
            NoSuchElementException: If there are no elements in the tree.

        Returns:
            The last element in the tree.
        """
        if self.root is None:
            raise NoSuchElementException("There are no elements in the tree.")
        return next(self.descendingIterator())

    def lower(self, key):
        """
        Returns the greatest element in this set strictly less than the given key.

        Args:
            key: The key to compare against.

        Returns:
            The greatest element in the set that is strictly less than the given key,
            or None if there is no such element.

        Raises:
            NullPointerException: If the key is None.
            ClassCastException: If the type of the key is not valid for this set.
        """
        if key is None:
            raise NullPointerException("Node cannot be None.")
        elif self.tree_type is not type(key):
            raise ClassCastException(
                f"The type of the node is not valid {self.tree_type}."
            )
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
        """
        Removes and returns the first (smallest) element in the TreeSet.

        Returns:
            The first element in the TreeSet, or None if the TreeSet is empty.
        """
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        self.remove(current.key)
        return current.key

    def pollLast(self):
        """
        Retrieves and removes the last (highest) element from the set.

        Returns:
            The last element in the set, or None if the set is empty.
        """
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right

        self.remove(current.key)
        return current.key

    def remove(self, key):
        """
        Removes the specified key from the TreeSet.

        Args:
            key: The key to be removed from the TreeSet.

        Returns:
            The removed key if it exists in the TreeSet, None otherwise.
        """
        return self.remove_node(self.find(key))

    def size(self):
        """
        Returns the number of elements in the TreeSet.

        Returns:
            int: The number of elements in the TreeSet.
        """
        return self._size_recursive(self.root)
