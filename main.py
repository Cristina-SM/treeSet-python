from TreeSet import TreeSet


def main():
    print("Treeset new")
    tree_set_new = TreeSet()

    tree_set_new.add("b")
    tree_set_new.add("a")
    tree_set_new.add("d")
    tree_set_new.add("c")
    tree_set_new.add("g")
    tree_set_new.add("f")
    tree_set_new.add("e")

    print(tree_set_new)
    print(tree_set_new.size())
    print(tree_set_new.contains("a"))
    iterador = tree_set_new.descendingIterator()
    # print(tree_set_new.__repr__)
    print("Iterador descendente")
    for _ in range(0, tree_set_new.size()):
        print(next(iterador))
    # new = tree_set_new.clone()
    # tree_set_new.remove("a")
    # print(tree_set_new.contains("a"))
    # print(tree_set_new)
    # print(new)
    # tree_set_new.clear()
    # print(tree_set_new)

    iter1 = tree_set_new.__iter__()
    print("Iterador normal")
    for _ in range(0, tree_set_new.size()):
        print(next(iter1))

    print("Método first")
    print(tree_set_new.first())

    print("Método isEmpty")
    print(tree_set_new.isEmpty())

    print("Método last")
    print(tree_set_new.last())

    print("Método lower")
    print(tree_set_new.lower("b"))

    print("Método floor")
    print(tree_set_new.floor("b"))

    print("Método higher")
    print(tree_set_new.higher("b"))

    print("Método pollLast")
    print(tree_set_new.pollLast())

    print("Método pollFirst")
    print(tree_set_new.pollFirst())
    
if __name__ == "__main__":
    main()
