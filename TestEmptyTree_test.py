import unittest

from NullPointerException import NullPointerException
from NoSuchElementException import NoSuchElementException
from TreeSet import TreeSet


class EmptyTree(unittest.TestCase):
    """
    Unit test case for the TreeSet class.

    This test suite contains unit tests to verify the functionality of the TreeSet class.
    The TreeSet is a collection that stores elements in a sorted, tree-based structure.
    """

    def setUp(self):
        """
        Sets up a new, empty TreeSet instance before each test.

        This method is called before every test case method to ensure each test
        has a fresh instance of TreeSet to work with.
        """
        self.tree = TreeSet(str)

    def testAdd(self):
        """
        Tests adding a new element to the TreeSet.

        This test verifies that adding a single element to the TreeSet works correctly.
        It ensures that the element is added and the size of the TreeSet is updated.
        """
        self.tree.add("a")
        self.assertTrue(
            self.tree.contains("a"), "The tree should contain the added element 'a'."
        )
        self.assertEqual(
            self.tree.size(),
            1,
            "The size of the tree should be 1 after adding one element.",
        )

    def testAddExistingElement(self):
        """
        Tests adding an existing element to the TreeSet.

        This test verifies that adding an element that already exists in the TreeSet
        does not increase the size of the TreeSet and does not add duplicates.
        """
        self.tree.add("b")
        self.tree.add("b")
        self.assertEqual(
            self.tree.size(),
            1,
            "The size of the tree should remain 1 after adding a duplicate element.",
        )

    def testCeilingNonExistingElement(self):
        """
        Tests the ceiling method with a non-existing element in the TreeSet.

        This test checks the behavior of the ceiling method when the TreeSet is empty
        or when the specified element is not present in the TreeSet.
        """
        self.assertEqual(
            self.tree.ceiling("a"),
            None,
            "The ceiling of a non-existing element should be None.",
        )

    def testClear(self):
        """
        Tests clearing all elements from the TreeSet.

        This test verifies that the clear method removes all elements from the TreeSet
        and that the size of the TreeSet is reset to zero.
        """
        self.tree.add("a")
        self.tree.clear()
        self.assertEqual(
            self.tree.size(),
            0,
            "The size of the tree should be 0 after clearing all elements.",
        )

    def testCloneNonExistingElements(self):
        """
        Tests cloning the TreeSet when it contains no elements.

        This test ensures that cloning an empty TreeSet produces another empty TreeSet
        and that the size of the cloned TreeSet is zero.
        """
        cloned_tree = self.tree.clone()
        self.assertEqual(
            cloned_tree.size(),
            0,
            "The cloned tree should have a size of 0 when cloning an empty tree.",
        )

    def testContains(self):
        """
        Tests the contains method for a non-existing element in the TreeSet.

        This test checks whether the contains method correctly identifies that an element
        is not present in the TreeSet.
        """
        self.assertFalse(
            self.tree.contains("a"),
            "The tree should not contain the element 'a' as it has not been added.",
        )

    def testDescendingIterator(self):
        """
        Test case for the descendingIterator method.

        This test case verifies that the descendingIterator method returns an empty iterator when the tree is empty.

        Steps:
        1. Create an empty tree.
        2. Call the descendingIterator method on the tree.
        3. Iterate over the iterator and append each element to a list.
        4. Assert that the list is empty.

        Expected behavior:
        - The descendingIterator method should return an empty iterator.
        - The list of elements should be empty.

        """
        self.iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(self.iterador))
        self.assertEqual(lista, [])
    
    def testFirstNonExistingElement(self):
        """
        Test case to verify that a NoSuchElementException is raised when calling the first() method on an empty tree.
        """
        self.assertRaises(NoSuchElementException, self.tree.first)
    
    def testFloorNonExistingElement(self):
        """
        Test case to verify the behavior of the floor method when the element does not exist in the tree.

        The floor method should return None when the specified element is not present in the tree.

        """
        self.assertEqual(self.tree.floor("a"), None)
    
    def testHigherNonExistingElement(self):
        """
        Test case to verify the behavior of the higher method when the element does not exist in the tree.

        The higher method should return None when there is no element in the tree that is strictly greater than the given element.

        """
        self.assertEqual(self.tree.higher("a"), None)
    
    def testIsEmpty(self):
        """
        Test case to check if the tree is empty.

        This method asserts that the `isEmpty` method of the `tree` object returns True,
        indicating that the tree is empty.
        """
        self.assertTrue(self.tree.isEmpty())

    def testIter(self):
        """
        Tests the iterator of the TreeSet.

        This test verifies that the iterator works correctly for an empty TreeSet.
        It checks that the iterator does not yield any elements and that the resulting list is empty.
        """
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(iter1))
        self.assertEqual(
            lista, [], "The iterator should yield an empty list for an empty tree."
        )


    def testLastNonExistingElement(self):
        """
        Test case to verify that the `last` method raises a `NoSuchElementException`
        when called on an empty tree.
        """
        self.assertRaises(NoSuchElementException, self.tree.last)

    def testLowerNonExistingElement(self):
        """
        Test case to verify the behavior of the lower method when the element does not exist in the tree.

        The lower method should return None when there is no element in the tree that is strictly less than the given element.

        """
        self.assertEqual(self.tree.lower("a"), None)

    def testPollFirst(self):
        """
        Test the pollFirst method of the tree.

        This method checks if the pollFirst method returns None when called on an empty tree.

        Returns:
            None
        """
        self.assertIsNone(self.tree.pollFirst())
    
    def testPollLast(self):
        """
        Test the `pollLast` method of the tree.

        This method checks if the `pollLast` method returns `None` when called on an empty tree.

        Returns:
            None
        """
        self.assertIsNone(self.tree.pollLast())

    def testRemoveNonExistingElement(self):
        """
        Tests removing a non-existing element from the TreeSet.

        This test ensures that attempting to remove an element that is not present in the TreeSet
        raises the appropriate exception and does not alter the size of the TreeSet.
        """
        with self.assertRaises(
            NullPointerException,
            msg="Removing a non-existing element should raise NullPointerException",
        ):
            self.tree.remove("a")
        self.assertEqual(
            self.tree.size(),
            0,
            "The size of the tree should remain 0 when trying to remove a non-existing element.",
        )

    def testSize(self):
        """
        Tests the size method of the TreeSet.

        This test verifies that the size method accurately returns the number of elements
        currently in the TreeSet. Initially, the size should be zero for a new TreeSet.
        """
        self.assertEqual(
            self.tree.size(),
            0,
            "The size of the tree should be 0 for a new, empty tree.",
        )

if __name__ == "__main__":
    unittest.main()
