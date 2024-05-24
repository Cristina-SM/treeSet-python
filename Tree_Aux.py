from ClassCastException import ClassCastException
from Node import Node
from NullPointerException import NullPointerException


class AVL_tree:
    class TreeAux:
        def __init__(self, tree_type):
            """
            Initializes a TreeAux object.

            Parameters:
            - tree_type (str): The type of the tree.

            Attributes:
            - root: The root node of the tree.
            - tree_type: The type of the tree.
            """
            self.root = None
            self.tree_type = tree_type

    def _add(self, key, node):
        """
        Adds a new node with the given key to the tree.

        Parameters:
        - key: The key of the node to be added.
        - node: The current node being inspected during the insertion process.

        Returns:
        None
        """
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
                node.left.parent = node
                self._inspect_insertion(node.left)
            else:
                self._add(key, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
                node.right.parent = node
                self._inspect_insertion(node.right)
            else:
                self._add(key, node.right)
        else:
            print(f"Key '{key}' is already in the tree\n")

    def _ceiling_recursive(self, node, value):
        """
        Recursively finds the smallest key in the tree that is greater than or equal to the given value.

        Args:
            node (Node): The current node being checked.
            value: The value to compare against.

        Returns:
            The smallest key in the tree that is greater than or equal to the given value, or None if no such key exists.
        """
        if node is None:
            return None
        if node.key == value:
            return node.key
        if node.key < value:
            return self._ceiling_recursive(node.right, value)

        left_result = self._ceiling_recursive(node.left, value)

        if left_result is not None:
            return left_result

        return node.key

    def height(self):
        """
        Returns the height of the tree.

        The height of a tree is defined as the maximum number of edges in any path from the root to a leaf node.

        Returns:
            int: The height of the tree. If the tree is empty, returns 0.
        """
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, node, height):
        """
        Calculates the height of a given node in the tree.

        Parameters:
        - node: The node for which to calculate the height.
        - height: The current height of the node.

        Returns:
        - The height of the node.

        """
        if node is None:
            return height
        left_height = self._height(node.left, height + 1)
        right_height = self._height(node.right, height + 1)
        return max(left_height, right_height)

    def find(self, key):
            """
            Finds the node with the given key in the tree.

            Parameters:
            - key: The key to search for in the tree.

            Returns:
            - The node with the given key if found, None otherwise.
            """
            if self.root is not None:
                return self._find(key, self.root)
            else:
                return None

    def _find(self, key, node):
            """
            Recursively finds a node with the given key in the tree.

            Args:
                key: The key to search for.
                node: The current node being checked.

            Returns:
                The node with the given key if found, otherwise None.
            """
            if key == node.key:
                return node
            elif key < node.key and node.left is not None:
                return self._find(key, node.left)
            elif key > node.key and node.right is not None:
                return self._find(key, node.right)
            return None

    def remove_node(self, node):
        """
        Removes a node from the tree.

        Args:
            node: The node to be removed.

        Returns:
            bool: True if the node was successfully removed, False otherwise.
        """
        if node is None:
            raise NullPointerException("Node to remove cannot be None\n")
        elif node is not None:
            if (
                node.__class__.__eq__ is object.__eq__
                and node.__class__.__lt__ is object.__lt__
                and self.tree_type is not type(node.key)
            ):
                raise ClassCastException(f"The type of the node to remove must be {self.tree_type}\n")
        if self.find(node.key) is None:
            print("Node not found\n")
            return False

        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        # Case 1: Node to remove has no children
        if node_children == 0:
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None

            else:
                self.root = None

        # Case 2: Node to remove has only a child
        if node_children == 1:
            next_node = None

            if node.left is not None:
                next_node = node.left
            else:
                next_node = node.right

            # In case node to remove is the root, swap node to remove with his child
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = next_node
                else:
                    node_parent.right = next_node
            else:
                self.root = next_node

            next_node.parent = node_parent

        # Case 3: Node to remove has two children
        if node_children == 2:
            successor = min_value_node(node.right)
            node.key = successor.key
            self.remove_node(successor)

            return True
        if node_parent is not None:
            node_parent.height = 1 + max(
                self.get_height(node_parent.left), self.get_height(node_parent.right)
            )
            self._inspect_deletion(node_parent)
        return False

    def search(self, key):
            """
            Searches for a given key in the tree.

            Parameters:
            - key: The key to search for.

            Returns:
            - True if the key is found in the tree, False otherwise.
            """
            if self.root is not None:
                return self._search(key, self.root)
            else:
                return False

    def _search(self, key, node):
        """
        Recursively searches for a key in the tree starting from the given node.

        Args:
            key: The key to search for.
            node: The current node being checked.

        Returns:
            True if the key is found in the tree, False otherwise.
        """
        if key == node.key:
            return True
        elif key < node.key and node.left is not None:
            return self._search(key, node.left)
        elif key > node.key and node.right is not None:
            return self._search(key, node.right)
        return False

    def _inspect_insertion(self, node, path=[]):
        """
        Inspects the insertion of a node in the tree and performs rebalancing if necessary.

        Args:
            node: The node being inserted.
            path: The path from the inserted node to the root of the tree.

        Returns:
            None
        """
        if node.parent is None:
            return
        path = [node] + path
        left_height = self.get_height(node.parent.left)
        right_height = self.get_height(node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + node.height
        if new_height > node.parent.height:
            node.parent.height = new_height
        self._inspect_insertion(node.parent, path)

    def _inspect_deletion(self, node):
        """
        Inspects the tree after a deletion operation to check if rebalancing is required.

        Args:
            node: The node to inspect.

        Returns:
            None
        """
        if node is None:
            return
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(node)
            x = self.taller_child(y)
            self._rebalance_node(node, y, x)

        self._inspect_deletion(node.parent)

    def _rebalance_node(self, z, y, x):
        """
        Rebalances the tree by performing rotation operations based on the configuration of nodes z, y, and x.

        Parameters:
        - z: The parent node of y.
        - y: The parent node of x.
        - x: The node being rebalanced.

        Raises:
        - Exception: If the configuration of nodes z, y, and x is not recognized.

        Returns:
        - None
        """
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception(
                "Rebalance error: z,y,x node configuration not recognized!"
            )

    def _right_rotate(self, z):
        """
        Performs a right rotation on the given node 'z' in the tree.

        Args:
            z: The node to be rotated.

        Returns:
            None
        """
        sub_root = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 is not None:
            t3.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def _left_rotate(self, z):
        """
        Performs a left rotation on the given node 'z' in the tree.

        Args:
            z: The node to be rotated.

        Returns:
            None
        """
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def taller_child(self, node):
        """
        Returns the child node with the greater height.

        Parameters:
        - node: The node for which to determine the taller child.

        Returns:
        - The child node with the greater height.
        """
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        if left >= right:
            return node.left
        else:
            return node.right

    def get_height(self, node):
        """
        Returns the height of the given node.

        Parameters:
        - node: The node for which to calculate the height.

        Returns:
        - The height of the node. If the node is None, returns 0.
        """
        if node is None:
            return 0
        return node.height

    def _size_recursive(self, node):
        """
        Recursively calculates the size of the tree rooted at the given node.

        Args:
            node: The root node of the tree.

        Returns:
            The size of the tree.

        """
        if node is None:
            return 0
        else:
            return (
                1 + self._size_recursive(node.left) + self._size_recursive(node.right)
            )

    def _clone_recursive(self, node):
        """
        Recursively clones a node and its children.

        Args:
            node (Node): The node to be cloned.

        Returns:
            Node: The cloned node.
        """
        if node is None:
            return None
        new_node = Node(node.key)
        new_node.parent = node.parent
        new_node.height = node.height
        new_node.left = self._clone_recursive(node.left)
        new_node.right = self._clone_recursive(node.right)
        return new_node

    def _search(self, key, node):
        """
        Recursively searches for a key in the tree starting from the given node.

        Args:
            key: The key to search for.
            node: The starting node for the search.

        Returns:
            True if the key is found in the tree, False otherwise.

        Raises:
            NullPointerException: If the given node is None.
        """
        if self.find(key) is None:
            return False
        if node is None:
            raise NullPointerException("Node to remove cannot be None")
        if key == node.key:
            return True
        if key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def _inorder_traversal(self, node, result):
        """
        Perform an inorder traversal of the tree starting from the given node.

        Args:
            node: The starting node for the traversal.
            result: A list to store the keys of the nodes in the traversal order.

        Returns:
            None
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def _inorder_generator(self, node):
            """
            Generates the keys of the tree in an inorder traversal.

            Args:
                node: The root node of the subtree to traverse.

            Yields:
                The keys of the tree in an inorder traversal.
            """
            if node is not None:
                yield from self._inorder_generator(node.left)
                yield node.key
                yield from self._inorder_generator(node.right)
