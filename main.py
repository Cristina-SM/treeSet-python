import time

from TreeSet import TreeSet


def main():
    print("Treeset main")


def test_times():
    with open("data/times.csv", mode="w", encoding="utf-8") as fw:
        size = 1
        print("size;miliseconds;seconds", file=fw)

        while size < 17 * 10**6:
            # Registro del tiempo de inicio
            tree = TreeSet(int)
            start_time = time.perf_counter()

            for i in range(size):
                tree.add(i)

            # Registro del tiempo de finalización
            end_time = time.perf_counter()
            duration = (end_time - start_time) * 1000
            print(f"Tiempo de ejecución ({size}):", duration, "milisegundos")

            print(
                f"{size};{round(duration, 3)};{round(duration / 1000, 3)}".replace(
                    ".", ","
                ),
                file=fw,
            )

            size <<= 1


if __name__ == "__main__":
    main()
    # test_times()
