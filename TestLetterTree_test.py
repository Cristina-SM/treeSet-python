import unittest


from TreeSet import TreeSet


class LetterTest(unittest.TestCase):
    """
    Unit test case for the TreeSet class with string elements.

    This test suite contains unit tests to verify the functionality of the TreeSet class
    when storing string elements.
    """

    def setUp(self):
        """
        Sets up a new TreeSet instance and adds string elements before each test.

        This method is called before every test case method to ensure each test
        has a fresh instance of TreeSet with predefined string elements.
        """
        self.tree = TreeSet(str)
        self.tree.add("b")
        self.tree.add("A")
        self.tree.add("d")
        self.tree.add("g")
        self.tree.add("m")
        self.tree.add("H")
        self.tree.add("a")
        self.tree.add("C")

    def testCeiling(self):
        """
        Tests the ceiling method for string elements in the TreeSet.

        This test checks whether the ceiling method correctly finds the smallest
        element greater than or equal to the specified string.
        """
        self.assertEqual(self.tree.ceiling("g"), "g")
        self.assertEqual(self.tree.ceiling("z"), None)

    def testClone(self):
        """
        Tests cloning the TreeSet containing string elements.

        This test ensures that cloning a TreeSet containing string elements produces
        another TreeSet with the same contents, and operations on the cloned TreeSet
        do not affect the original TreeSet.
        """
        self.ntree = self.tree.clone()
        self.assertEqual(
            self.ntree.size(),
            8,
            "The cloned tree should have the same size as the original tree.",
        )
        self.ntree.clear()
        self.assertTrue(
            self.ntree.isEmpty(), "Clearing the cloned tree should make it empty."
        )

    def testClearClone(self):
        """
        Tests clearing the cloned TreeSet.

        This test verifies that clearing the cloned TreeSet does not affect the
        original TreeSet.
        """
        self.new = self.tree.clone()
        self.new.clear()
        self.assertTrue(
            self.new.isEmpty(), "The cloned tree should be empty after clearing."
        )
        self.assertFalse(
            self.tree.isEmpty(), "The original tree should not be affected."
        )

    def testContains(self):
        """
        Tests the contains method for string elements in the TreeSet.

        This test checks whether the contains method correctly identifies whether
        a string element is present in the TreeSet.
        """
        self.assertTrue(
            self.tree.contains("b"), "The tree should contain the specified string."
        )
        self.assertFalse(
            self.tree.contains("z"), "The tree should not contain the specified string."
        )

    def testDescendingIterator(self):
        """
        Tests the descendingIterator method of the TreeSet.

        This test verifies that the descendingIterator returns an iterator
        over the elements in the TreeSet in descending order.
        """
        self.iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(self.iterador))
        self.assertEqual(
            lista,
            ["m", "g", "d", "b", "a", "H", "C", "A"],
            "The elements should be in descending order.",
        )

    def testFirst(self):
        """
        Tests retrieving the first string element from the TreeSet.

        This test verifies that the first method returns the smallest string
        element in the TreeSet.
        """
        self.assertEqual(
            self.tree.first(), "A", "The first element should be the smallest string."
        )

    def testFloor(self):
        """
        Tests the floor method for string elements in the TreeSet.

        This test checks whether the floor method correctly finds the largest
        element less than or equal to the specified string.
        """
        self.assertEqual(self.tree.floor("g"), "g")

    def testHigher(self):
        """
        Tests the higher method for string elements in the TreeSet.

        This test checks whether the higher method correctly finds the smallest
        element greater than the specified string.
        """
        self.assertEqual(self.tree.higher("g"), "m")

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
        self.iterador = self.tree.__iter__()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(self.iterador))
        self.assertEqual(
            lista,
            ["A", "C", "H", "a", "b", "d", "g", "m"],
            "The elements should be in ascending order.",
        )

    def testLast(self):
        """
        Tests retrieving the last string element from the TreeSet.

        This test verifies that the last method returns the largest string
        element in the TreeSet.
        """
        self.assertEqual(
            self.tree.last(), "m", "The last element should be the largest string."
        )

    def testLower(self):
        """
        Tests the lower method for string elements in the TreeSet.

        This test checks whether the lower method correctly finds the largest
        element less than the specified string.
        """
        self.assertEqual(self.tree.lower("g"), "d")

    def testRemoveLetter(self):
        """
        Tests removing a string element from the TreeSet.

        This test verifies that removing a string element from the TreeSet
        works correctly.
        """
        self.assertTrue(
            self.tree.contains("a"), "The tree should contain the specified string."
        )
        self.tree.remove("a")
        self.assertFalse(
            self.tree.contains("a"), "The tree should not contain the removed string."
        )

    def testSize(self):
        """
        Tests retrieving the size of the TreeSet.

        This test verifies that the size method accurately returns the number of string elements
        currently in the TreeSet.
        """
        self.assertEqual(self.tree.size(), 8, "The size of the tree should be 8.")

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
            "['C', 'H', 'a', 'b', 'd', 'g']",
            "The string representation should match.",
        )
        self.assertEqual(
            self.tree.size(), 6, "The size of the tree should be 6 after polling."
        )


if __name__ == "__main__":
    unittest.main()
