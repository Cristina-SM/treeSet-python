from TreeSet import TreeSet
import time


def main():
    print("Treeset new")
    tree_set_new = TreeSet()
    tree_set_new.add("b")
    tree_set_new.add(1)
    tree_set_new.add("d")
    # tree_set_new.add("g")
    # tree_set_new.add("m")
    # tree_set_new.add("H")
    # tree_set_new.add("a")
    # tree_set_new.add("C")

    print(tree_set_new)
    print(tree_set_new.size())
    print(tree_set_new.contains("a"))
    iterador = tree_set_new.descendingIterator()
    print(tree_set_new.__repr__)
    pepe = tree_set_new.clone()
    print(pepe.__repr__)
    print("Iterador descendente")
    for _ in range(0, tree_set_new.size()):
        print(next(iterador))
    # new = tree_set_new.clone()
    tree_set_new.remove("b")
    # print(tree_set_new.contains("a"))
    # print(tree_set_new)
    # print(new)
    # tree_set_new.clear()
    # print(tree_set_new)

    print("Método ceiling")
    print(tree_set_new.ceiling("b"))

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

    print("Lista actualizada")
    print(tree_set_new)

def test_times():
    with open("data/times.csv", mode="w", encoding="utf-8") as fw:
        size = 1
        print("size;miliseconds;seconds", file=fw)

        while size < 17 * 10 ** 6:
            # Registro del tiempo de inicio
            tree = TreeSet()
            start_time = time.perf_counter()

            for i in range(size):
                tree.add(i)

            # Registro del tiempo de finalización
            end_time = time.perf_counter()
            duration = (end_time - start_time) * 1000
            print("Tiempo de ejecución:", duration, "milisegundos")

            print(f"{size};{round(duration, 3)};{round(duration / 1000, 3)}".replace(".", ","), file=fw)

            size <<= 1

if __name__ == "__main__":
    main()
    #test_times()
