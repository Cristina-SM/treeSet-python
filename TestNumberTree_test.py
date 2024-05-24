import unittest

from TreeSet import TreeSet


class NumberTest(unittest.TestCase):
    """
    Unit test case for the TreeSet class with integer elements.

    This test suite contains unit tests to verify the functionality of the TreeSet class
    when storing integer elements.
    """

    def setUp(self):
        """
        Sets up a new TreeSet instance and adds integer elements before each test.

        This method is called before every test case method to ensure each test
        has a fresh instance of TreeSet with predefined integer elements.
        """
        self.tree = TreeSet(int)
        self.tree.add(1)
        self.tree.add(53)
        self.tree.add(36)
        self.tree.add(70)
        self.tree.add(7)
        self.tree.add(45)
        self.tree.add(11)

    def testCeiling(self):
        """
        Tests the ceiling method for integer elements in the TreeSet.

        This test checks whether the ceiling method correctly finds the smallest
        element greater than or equal to the specified integer.
        """
        self.assertEqual(self.tree.ceiling(36), 36)
        self.assertEqual(self.tree.ceiling(37), 45)

    def testClone(self):
        """
        Tests cloning the TreeSet containing integer elements.

        This test ensures that cloning a TreeSet containing integer elements produces
        another TreeSet with the same contents, and operations on the cloned TreeSet
        do not affect the original TreeSet.
        """
        self.ntree = self.tree.clone()
        self.assertEqual(
            self.ntree.size(),
            7,
            "The cloned tree should have the same size as the original tree.",
        )
        self.ntree.clear()
        self.assertTrue(
            self.ntree.isEmpty(), "Clearing the cloned tree should make it empty."
        )

    def testContains(self):
        """
        Tests the contains method for integer elements in the TreeSet.

        This test checks whether the contains method correctly identifies whether
        an integer element is present in the TreeSet.
        """
        self.assertTrue(
            self.tree.contains(1), "The tree should contain the specified integer."
        )
        self.assertFalse(
            self.tree.contains(100),
            "The tree should not contain the specified integer.",
        )

    def testDescendingIterator(self):
        """
        Tests the descendingIterator method of the TreeSet.

        This test verifies that the descendingIterator returns an iterator
        over the elements in the TreeSet in descending order.
        """
        iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iterador))
        self.assertEqual(
            lista,
            [70, 53, 45, 36, 11, 7, 1],
            "The elements should be in descending order.",
        )

    def testFirst(self):
        """
        Tests retrieving the first integer element from the TreeSet.

        This test verifies that the first method returns the smallest integer
        element in the TreeSet.
        """
        self.assertEqual(
            self.tree.first(), 1, "The first element should be the smallest integer."
        )

    def testFloor(self):
        """
        Tests the floor method for integer elements in the TreeSet.

        This test checks whether the floor method correctly finds the largest
        element less than or equal to the specified integer.
        """
        self.assertEqual(self.tree.floor(36), 36)

    def testHigher(self):
        """
        Tests the higher method for integer elements in the TreeSet.

        This test checks whether the higher method correctly finds the smallest
        element greater than the specified integer.
        """
        self.assertEqual(self.tree.higher(36), 45)

    def testIsEmpty(self):
        """
        Tests whether the TreeSet is empty.

        This test checks whether the isEmpty method correctly identifies whether
        the TreeSet is empty.
        """
        self.assertFalse(self.tree.isEmpty(), "The tree should not be empty.")

    def testIter(self):
        """
        Tests the iterator of the TreeSet.

        This test verifies that the iterator returns an iterator over the elements
        in the TreeSet in ascending order.
        """
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iter1))
        self.assertEqual(
            lista,
            [1, 7, 11, 36, 45, 53, 70],
            "The elements should be in ascending order.",
        )

    def testLast(self):
        """
        Tests retrieving the last integer element from the TreeSet.

        This test verifies that the last method returns the largest integer
        element in the TreeSet.
        """
        self.assertEqual(
            self.tree.last(), 70, "The last element should be the largest integer."
        )

    def testLower(self):
        """
        Tests the lower method for integer elements in the TreeSet.

        This test checks whether the lower method correctly finds the largest
        element less than the specified integer.
        """
        self.assertEqual(self.tree.lower(36), 11)

    def testRemoveNumber(self):
        """
        Tests removing an integer element from the TreeSet.

        This test verifies that removing an integer element from the TreeSet
        works correctly.
        """
        self.assertTrue(
            self.tree.contains(36), "The tree should contain the specified integer."
        )
        self.tree.remove(36)
        self.assertFalse(
            self.tree.contains(36), "The tree should not contain the removed integer."
        )

    def testTreeAfterPoll(self):
        """
        Tests the TreeSet after polling the first and last elements.

        This test polls the first and last elements from the TreeSet and checks
        whether the size and string representation of the TreeSet are updated correctly.
        """
        self.tree.pollFirst()
        self.tree.pollLast()
        self.assertEqual(
            self.tree.__str__(),
            "['7', '11', '36', '45', '53']",
            "The string representation should match.",
        )
        self.assertEqual(
            self.tree.size(), 5, "The size of the tree should be 5 after polling."
        )


if __name__ == "__main__":
    unittest.main()
