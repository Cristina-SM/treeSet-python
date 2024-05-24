import tkinter as tk
from tkinter import *

from ClassCastException import ClassCastException
from TreeSet import TreeSet


class TreesetApp(tk.Tk):
    def __init__(self):
        """
        Initializes the Interface class.

        This method sets up the user interface for the Treeset application.
        It creates a Tkinter window, sets its geometry, and initializes various UI elements such as labels, buttons, and canvas.

        Parameters:
        None

        Returns:
        None
        """
        self.master = Tk()
        self.master.geometry("800x800")
        self.tree = TreeSet(tree_type)
        self.master.title("Treeset")
        self.canvas = tk.Canvas(self.master, width=800, height=500, bg="white")
        self.canvas.pack()

        self.label = Label(self.master, text="Treeset", width=12)
        self.label.pack(anchor="n")

        self.entry = Entry(
            self.master,
            width=10,
        )
        self.entry.pack(anchor="n")

        self.greet_button = Button(
            self.master, text="Add", command=self.add, width=10, borderwidth=5
        )
        self.greet_button.pack(anchor="n")

        self.close_button = Button(
            self.master, text="Remove", command=self.remove, width=10, borderwidth=5
        )
        self.close_button.pack(anchor="n")

        self.close_button = Button(
            self.master, text="Contains", command=self.contains, width=10, borderwidth=5
        )
        self.close_button.pack(anchor="n")

        self.close_button = Button(
            self.master, text="Size", command=self.size, width=10, borderwidth=5
        )
        self.close_button.pack(anchor="n")

        self.close_button = Button(
            self.master, text="Clear", command=self.clear, width=10, borderwidth=5
        )
        self.close_button.pack(anchor="n")

        self.close_button = Button(
            self.master, text="Exit", command=self.master.quit, width=10, borderwidth=5
        )
        self.close_button.pack(anchor="n")

    def add(self):
        """
        Adds an element to the tree set.

        This method takes the value from the entry field and creates a new tree_type object with it.
        The new object is then added to the tree set and the canvas is updated.

        Parameters:
        None

        Returns:
        None
        """
        data = tree_type(self.entry.get())
        self.tree.add(data)
        self.update_canvas()

    def remove(self):
        """
        Removes the specified data from the tree.

        This method removes the data specified by the entry field from the tree. It first creates a new instance of the tree type using the value entered in the entry field. Then, it calls the `remove` method of the tree object to remove the data from the tree. Finally, it updates the canvas to reflect the changes made to the tree.

        Parameters:
        None

        Returns:
        None
        """
        data = tree_type(self.entry.get())
        self.tree.remove(data)
        self.update_canvas()

    def contains(self):
        """
        Checks if the tree contains a specific element.

        Returns:
            None
        """
        print(self.tree.contains(tree_type(self.entry.get())))

    def size(self):
            """
            Returns the number of elements in the tree set.

            Returns:
                int: The number of elements in the tree set.
            """
            print(self.tree.size())

    def clear(self):
        """
        Clears all elements from the tree set.
        """
        self.tree.clear()
        self.update_canvas()

    def update_canvas(self):
        """
        Clears the canvas and redraws the tree on it.

        This method deletes all existing items on the canvas and then calls the `draw_tree` method
        to redraw the tree on the canvas.

        Parameters:
        - None

        Returns:
        - None
        """
        self.canvas.delete("all")
        self.draw_tree(self.tree.root, 400, 30, 200)

    def draw_tree(self, node, x, y, x_offset):
        """
        Draws a binary tree on a canvas.

        Parameters:
        - node: The root node of the binary tree to be drawn.
        - x: The x-coordinate of the current node.
        - y: The y-coordinate of the current node.
        - x_offset: The horizontal offset between nodes.

        Returns:
        None
        """
        if node is not None:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.key))
            if node.left:
                self.canvas.create_line(x, y, x - x_offset, y + 50)
                self.draw_tree(node.left, x - x_offset, y + 50, x_offset // 2)
            if node.right:
                self.canvas.create_line(x, y, x + x_offset, y + 50)
                self.draw_tree(node.right, x + x_offset, y + 50, x_offset // 2)


if __name__ == "__main__":
    tree_type = input("Introduce un ejemplo del tipo del árbol: ")
    if tree_type == "str":
        tree_type = str
    elif tree_type == "int":
        tree_type = int
    elif tree_type == "float":
        tree_type = float
    else:
        ClassCastException("Tipo no válido")
        exit()

    my_gui = TreesetApp()
    my_gui.master.mainloop()