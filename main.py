from TreeSet import TreeSet
from treesetOld import TreeSetOld


def main():
    print("TreeSet Example")
    # Create a new TreeSet
    tree_set = TreeSetOld()

    # Add some values to the TreeSet
    tree_set.add("b")
    tree_set.add("a")
    tree_set.add("c")
    tree_set.add("d")
    tree_set.add("e")
    tree_set.add("f")
    tree_set.add("g")
    print(tree_set)
    print(tree_set.size())
    print(tree_set.contains("a"))
    print(tree_set.descendingIterator())
    print(tree_set.remove("a"))
    print(tree_set.contains("a"))
    print(tree_set)
    tree_set.clear()
    print(tree_set)

    # tree_set.add(1)
    # tree_set.add(7)
    print(tree_set)  # Output: 1, 3, 5, 7, 8

    # # Check if the TreeSet contains a value
    # print(tree_set.contains(3))  # Output: True
    # print(tree_set.contains(6))  # Output: False

    # # Remove a value from the TreeSet
    # tree_set.remove(5)

    # Print the TreeSet
    # print(tree_set)  # Output: 1, 3, 7, 8

    print("Treeset new")
    tree_set_new = TreeSet()

    tree_set_new.add("a")
    tree_set_new.add("b")
    tree_set_new.add("c")
    tree_set_new.add("d")
    tree_set_new.add("e")
    tree_set_new.add("f")
    tree_set_new.add("g")

    print(tree_set_new)
    print(tree_set_new.size())
    print(tree_set_new.contains("a"))
    iterador = tree_set_new.descendingIterator()
    # print(tree_set_new.__repr__)
    for i in range(0, tree_set_new.size()):
        print(next(iterador))

    tree_set_new.remove("a")
    print(tree_set_new.contains("a"))
    print(tree_set_new)
    tree_set_new.clear()
    print(tree_set_new)


if __name__ == "__main__":
    main()
