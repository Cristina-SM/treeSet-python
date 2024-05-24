import tkinter as tk
from tkinter import *

from ClassCastException import ClassCastException
from TreeSet import TreeSet


class TreesetApp(tk.Tk):
    def __init__(self):
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
        data = tree_type(self.entry.get())
        self.tree.add(data)
        self.update_canvas()

    def remove(self):
        data = tree_type(self.entry.get())
        self.tree.remove(data)
        self.update_canvas()

    def contains(self):
        print(self.tree.contains(tree_type(self.entry.get())))

    def size(self):
        print(self.tree.size())

    def clear(self):
        self.tree.clear()
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        self.draw_tree(self.tree.root, 400, 30, 200)

    def draw_tree(self, node, x, y, x_offset):
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
    tree_type = input("Enter the tree type: ")
    if tree_type == "str":
        tree_type = str
    elif tree_type == "int":
        tree_type = int
    elif tree_type == "float":
        tree_type = float
    else:
        raise ClassCastException("Invalid type")
        exit()

    my_gui = TreesetApp()
    my_gui.master.mainloop()
