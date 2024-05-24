import unittest

from TreeSet import TreeSet


class NumberTest(unittest.TestCase):
    """
    Unit test case for the TreeSet class.

    This test suite contains unit tests to verify the functionality of the TreeSet class
    when storing float elements.
    """

    def setUp(self):
        """
        Set up the test environment by creating a TreeSet object and adding elements to it.
        """
        self.tree = TreeSet(float)
        self.tree.add(1.2)
        self.tree.add(5.3)
        self.tree.addAll([3.16, 7.0, 7.1, 45.2, 1.3])

    def testAdd(self):
        """
        Test case for the add method of the TreeFloat class.

        This test verifies that the add method returns False when adding a single element to the tree,
        and also when adding multiple elements using the addAll method.

        """
        self.assertFalse(self.tree.add(5.3))
        self.assertFalse(self.tree.addAll([3.16, 7.0, 7.1, 45.2, 1.3]))

    def testCeiling(self):
        """
        Test the ceiling method of the Tree class.

        The ceiling method should return the smallest element in the tree that is greater than or equal to the given value.

        This test case checks if the ceiling method returns the expected results for different input values.

        """
        self.assertEqual(self.tree.ceiling(3.16), 3.16)
        self.assertEqual(self.tree.ceiling(3.17), 5.3)

    def testClone(self):
        """
        Test case for the clone method of the Tree class.

        This test verifies that the clone method creates a new tree object that is an exact copy of the original tree.
        It checks the size of the cloned tree and asserts that it is equal to the size of the original tree.
        It then clears the cloned tree and verifies that it is empty.

        """
        self.ntree = self.tree.clone()
        self.assertEqual(self.ntree.size(), 7)
        self.ntree.clear()
        self.assertTrue(self.ntree.isEmpty())

    def testContains(self):
        """
        Test case to check the 'contains' method of the tree.

        It asserts that the tree contains the value 1.2 and does not contain the value 100.0.
        """
        self.assertTrue(self.tree.contains(1.2))
        self.assertFalse(self.tree.contains(100.0))

    def testDescendingIterator(self):
        """
        Test the descendingIterator method of the tree.

        This method iterates over the elements of the tree in descending order and
        verifies that the elements are returned correctly.

        It creates an iterator using the descendingIterator method of the tree and
        adds each element to a list. Finally, it asserts that the list of elements
        matches the expected descending order.

        """
        iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iterador))
        self.assertEqual(lista, [45.2, 7.1, 7.0, 5.3, 3.16, 1.3, 1.2])

    def testFirst(self):
        """
        Test case for the first() method of the Tree class.

        This test verifies that the first element returned by the first() method
        of the Tree class is equal to 1.2.

        """
        self.assertEqual(self.tree.first(), 1.2)

    def testFloor(self):
        """
        Test the floor method of the TreeFloat class.

        The floor method should return the largest element in the tree that is less than or equal to the given value.

        This test case checks if the floor method returns the correct result for different input values.

        """
        self.assertEqual(self.tree.floor(3.16), 3.16)
        self.assertEqual(self.tree.floor(3.17), 3.16)

    def testHigher(self):
        """
        Test case to verify the behavior of the higher method in the Tree class.

        This test case checks if the higher method returns the correct value when called with a float value.
        It asserts that the returned value is equal to 5.3 when the input value is 3.16.
        """
        self.assertEqual(self.tree.higher(3.16), 5.3)

    def testIsEmpty(self):
        """
        Test case to check if the tree is empty.

        This method asserts that the `isEmpty` method of the `tree` object returns False.
        """
        self.assertFalse(self.tree.isEmpty())

    def testIter(self):
        """
        Test the iteration functionality of the tree.

        This method tests the __iter__() method of the tree by iterating over the elements
        and appending them to a list. It then asserts that the list contains the expected
        elements in the correct order.

        """
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iter1))
        self.assertEqual(lista, [1.2, 1.3, 3.16, 5.3, 7.0, 7.1, 45.2])

    def testLast(self):
        """
        Test case to verify the behavior of the last() method in the Tree class.

        The last() method should return the last element in the tree set.

        This test case asserts that the last element returned by the last() method is equal to 45.2.
        """
        self.assertEqual(self.tree.last(), 45.2)

    def testLower(self):
        """
        Test the lower() method of the tree.

        This method asserts that the lower() method returns the correct value when given a float argument.
        """
        self.assertEqual(self.tree.lower(3.16), 1.3)

    def testTreeAfterPoll(self):
        """
        Test case to verify the behavior of the tree after calling the pollFirst, pollLast, __str__, and size methods.

        This test case performs the following assertions:
        - Checks if the first element returned by pollFirst is equal to 1.2
        - Checks if the last element returned by pollLast is equal to 45.2
        - Checks if the string representation of the tree is equal to "['1.3', '3.16', '5.3', '7.0', '7.1']"
        - Checks if the size of the tree is equal to 5
        """
        self.assertEqual(self.tree.pollFirst(), 1.2)
        self.assertEqual(self.tree.pollLast(), 45.2)
        self.assertEqual(self.tree.__str__(), "['1.3', '3.16', '5.3', '7.0', '7.1']")
        self.assertEqual(self.tree.size(), 5)

    def testRemoveNumber(self):
        """
        Test case to verify the removal of a number from the tree.

        It checks if the number 3.16 is initially present in the tree using the `contains` method.
        Then, it removes the number 3.16 from the tree using the `remove` method.
        Finally, it checks if the number 3.16 is no longer present in the tree using the `contains` method.
        """
        self.assertTrue(self.tree.contains(3.16))
        self.tree.remove(3.16)
        self.assertFalse(self.tree.contains(3.16))

    def testSize(self):
        """
        Test case to verify the size() method of the tree.

        This test case asserts that the size() method of the tree returns the expected size, which is 7 in this case.
        """
        self.assertEqual(self.tree.size(), 7)


if __name__ == "__main__":
    unittest.main()
