from ClassCastException import ClassCastException
from Nodo import Node
from NullPointerException import NullPointerException


class TreeSet:

    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root is None:
            return ""
        content = "\n"  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = " " * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0:
                break
            cur_row = " "
            next_row = ""
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n is None:
                    cur_row += "   " + sep
                    next_row += "   " + sep
                    next_nodes.extend([None, None])
                    continue

                if n.key is not None:
                    buf = " " * int((5 - len(str(n.key))) / 2)
                    cur_row += "%s%s%s" % (buf, str(n.key), buf) + sep
                else:
                    cur_row += " " * 5 + sep

                if n.left is not None:
                    next_nodes.append(n.left)
                    next_row += " /" + sep
                else:
                    next_row += "  " + sep
                    next_nodes.append(None)

                if n.right is not None:
                    next_nodes.append(n.right)
                    next_row += "\ " + sep
                else:
                    next_row += "  " + sep
                    next_nodes.append(None)

            content += (
                cur_height * "   "
                + cur_row
                + "\n"
                + cur_height * "   "
                + next_row
                + "\n"
            )
            cur_nodes = next_nodes
            sep = " " * int(len(sep) / 2)  # cut separator size in half
        return content

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    # Funcion para obtener la altura de un nodo
    def _height(self, node, height):
        if node is None:
            return height
        left_height = self._height(node.left, height + 1)
        right_height = self._height(node.right, height + 1)
        return max(left_height, right_height)

    def find(self, key):
        if self.root is not None:
            return self._find(key, self.root)
        else:
            return None

    # Funcion para buscar un nodo
    def _find(self, key, node):
        if key == node.key:
            return node
        elif key < node.key and node.left is not None:
            return self._find(key, node.left)
        elif key > node.key and node.right is not None:
            return self._find(key, node.right)
        return None

    def remove_node(self, node):
        # Comprobar si el nodo a eliminar existe
        if node is None or self.find(node.key) is None:
            print("No se encuentra el nodo a eliminar")
            return False

        # Funcion para obtener el nodo con el valor minimo
        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        # Funcion para obtener el numero de hijos de un nodo
        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        # Obtenemos el nodo padre del nodo a eliminar
        node_parent = node.parent
        # Obtenemos el numero de hijos del nodo a eliminar
        node_children = num_children(node)

        # Caso 1: El nodo a eliminar no tiene hijos
        if node_children == 0:
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None

            else:
                self.root = None
        # Caso 2: El nodo a eliminar tiene solo un hijo
        if node_children == 1:
            next_node = None

            if node.left is not None:
                next_node = node.left
            else:
                next_node = node.right

            # En el caso de que el nodo a eliminar sea la raiz
            # Reemplazamos el nodo a eliminar por su hijo
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = next_node
                else:
                    node_parent.right = next_node
            else:
                self.root = next_node

            next_node.parent = node_parent

        # Caso 3: El nodo a eliminar tiene dos hijos
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

    def search(self, key):
        if self.root is not None:
            return self._search(key, self.root)
        else:
            return False

    def _search(self, key, node):
        if key == node.key:
            return True
        elif key < node.key and node.left is not None:
            return self._search(key, node.left)
        elif key > node.key and node.right is not None:
            return self._search(key, node.right)
        return False

    def _inspect_insertion(self, node, path=[]):
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
                "Rebalance error: la configuracio de z,y,x no esta reconocida"
            )

    def _right_rotate(self, z):
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
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        if left >= right:
            return node.left
        else:
            return node.right

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        if node is None:
            return 0
        else:
            return (
                1 + self._size_recursive(node.left) + self._size_recursive(node.right)
            )

    def _clone_recursive(self, node):
        if node is None:
            return None
        new_node = Node(node.key)
        new_node.left = self._clone_recursive(node.left)
        new_node.right = self._clone_recursive(node.right)
        return new_node

    def _search(self, key, node):

        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def _inorder_generator(self, node):
        if node is not None:
            yield from self._inorder_generator(node.left)
            yield node.key
            yield from self._inorder_generator(node.right)

    ### OBLIGATORIOS PARA EL TRABAJO

    # Función para insertar un nodo en el árbol
    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return True
        elif self.root is not None and self.root.key.__class__ != key.__class__:
            raise ClassCastException(
                f"El elemento no es del tipo {self.root.key.__class__}."
            )
        elif key is None:
            raise NullPointerException("El elemento a introducir no puede ser nulo")
        elif self.find(key) is None:
            self._add(key, self.root)
            return True
        return False

    # Subfunción para insertar
    def _add(self, key, node):
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
            print(f"El valor {key} ya esta en el arbol")

    # Funcion para eliminar un nodo
    def remove(self, key):
        return self.remove_node(self.find(key))

    def contains(self, key):
        return self._search(key, self.root)

    def descendingIterator(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return reversed(elements)

    def clear(self):
        self.root = None
        self._size = 0

    def clone(self):
        cloned_tree_set = TreeSet()
        # Llamar a una función auxiliar para clonar el árbol
        cloned_tree_set.root = self._clone_recursive(self.root)
        cloned_tree_set.size = self.size

        return cloned_tree_set

    def ceiling(self, value):
        return self._ceiling_recursive(self.root, value)

    def _ceiling_recursive(self, node, value):
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

    def pollLast(self):
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right

        self.remove(current.key)
        return current.key

    def pollFirst(self):
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        self.remove(current.key)
        return current.key

    def __str__(self):
        # Método para imprimir el TreeSet en orden
        elements = []
        self._inorder_traversal(self.root, elements)
        if len(elements) == 0:
            return "[]"
        return "['" + "', '".join(map(str, elements)) + "']"

    ### juanqui pruebas //__iter__, first, last, isEmpty,
    def __iter__(self):
        return self._inorder_generator(self.root)

    def first(self):
        return next(iter(self))

    def last(self):
        return next(self.descendingIterator())

    def isEmpty(self):
        return self.root is None

    def lower(self, key):
        current = self.root
        lower = None
        while current is not None:
            if current.key < key:
                lower = current.key
                current = current.right
            else:
                current = current.left
        return lower

    def floor(self, key):
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
        current = self.root
        higher = None
        while current is not None:
            if current.key > key:
                higher = current.key
                current = current.left
            else:
                current = current.right
        return higher
