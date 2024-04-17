from TreeSet import TreeSet
from Nodo import Node

def main():
            print("TreeSet Example")
            # Create a new TreeSet
            tree_set = TreeSet()

            # Add some values to the TreeSet
            tree_set.add("b")
            tree_set.add("a")
            tree_set.add("c")
            print(tree_set.remove("b"))
            # tree_set.add(1)
            # tree_set.add(7)
            print(tree_set)  # Output: 1, 3, 5, 7, 8

            # # Check if the TreeSet contains a value
            # print(tree_set.contains(3))  # Output: True
            # print(tree_set.contains(6))  # Output: False

            # # Remove a value from the TreeSet
            # tree_set.remove(5)

            # Print the TreeSet
            #print(tree_set)  # Output: 1, 3, 7, 8

if __name__ == "__main__":
        main()
