import unittest

from Car import Car
from NullPointerException import NullPointerException
from TreeSet import TreeSet


class TestCoche(unittest.TestCase):
    """
    Unit test case for the Car class.

    This test suite contains unit tests to verify the functionality of the Car class,
    which represents a collection of cars stored in a TreeSet data structure.
    """

    def setUp(self):
        """
        Sets up a new, empty TreeSet instance and some Car instances before each test.

        This method is called before every test case method to ensure each test
        has a fresh instance of TreeSet and some Car instances to work with.
        """
        self.tree = TreeSet(Car)
        self.coche = Car("4578LMZ")
        self.coche2 = Car("555ftg")
        self.coche3 = Car("2829abc")
        self.coche4 = Car("2384jkl")

    def test_addCoche(self):
        """
        Tests adding a Coche instance to the TreeSet.

        This test verifies that adding a Coche instance to the TreeSet works correctly.
        """
        self.assertTrue(
            self.tree.add(self.coche), "Adding a Coche instance should return True."
        )
        self.assertFalse(
            self.tree.remove(self.coche),
            "Removing a Coche instance that exists should return False.",
        )

    def testClone(self):
        """
        Tests cloning the TreeSet containing Coche instances.

        This test ensures that cloning a TreeSet containing Coche instances produces
        another TreeSet with the same contents, and operations on the cloned TreeSet
        do not affect the original TreeSet.
        """
        self.tree.add(self.coche2)
        self.tree.add(self.coche3)
        self.ntree = self.tree.clone()
        self.assertEqual(
            self.ntree.size(),
            2,
            "The cloned tree should have the same size as the original tree.",
        )
        self.ntree.add(self.coche4)
        self.assertEqual(
            self.ntree.size(),
            3,
            "Adding a Coche to the cloned tree should increase its size.",
        )
        self.ntree.clear()
        self.assertTrue(
            self.ntree.isEmpty(), "Clearing the cloned tree should make it empty."
        )

    def testContains(self):
        """
        Tests the contains method for Coche instances in the TreeSet.

        This test checks whether the contains method correctly identifies whether
        a Coche instance is present in the TreeSet.
        """
        self.assertFalse(
            self.tree.contains(Car("2829abc")),
            "The tree should not contain the specified Coche instance.",
        )
        self.assertFalse(
            self.tree.contains(Car("2384jkl")),
            "The tree should not contain the specified Coche instance.",
        )

    def testFirst(self):
        """
        Tests retrieving the first Coche instance from the TreeSet.

        This test verifies that the first method returns the first Coche instance
        in the TreeSet.
        """
        self.tree.add(self.coche)
        self.assertEqual(
            self.tree.first(),
            "4578LMZ",
            "The first Coche instance should be '4578LMZ'.",
        )

    def testLast(self):
        """
        Tests retrieving the last Coche instance from the TreeSet.

        This test verifies that the last method returns the last Coche instance
        in the TreeSet.
        """
        self.tree.add(self.coche)
        self.tree.add(self.coche2)
        self.assertEqual(
            self.tree.last(), "555ftg", "The last Coche instance should be '555ftg'."
        )

    def testNullPointer(self):
        """
        Tests adding and removing None and invalid Coche instances from the TreeSet.

        This test ensures that adding None or invalid Coche instances to the TreeSet
        raises the appropriate NullPointerException, and removing an invalid Coche
        instance does not affect the TreeSet.
        """
        with self.assertRaises(NullPointerException):
            self.tree.add(None)
        with self.assertRaises(NullPointerException):
            self.tree.remove("6952rtr")

    def testSize(self):
        """
        Tests retrieving the size of the TreeSet.

        This test verifies that the size method accurately returns the number of Coche instances
        currently in the TreeSet. Initially, the size should be zero for a new TreeSet.
        """
        self.assertEqual(
            self.tree.size(),
            0,
            "The size of the tree should be 0 for a new, empty tree.",
        )

    def testTreeAfterPoll(self):
        """
        Tests the TreeSet after polling the first and last Coche instances.

        This test adds several Coche instances to the TreeSet and then polls the first
        and last elements. It verifies that the size of the TreeSet is updated correctly
        after each poll operation.
        """
        self.tree.add(self.coche)
        self.tree.add(self.coche2)
        self.tree.add(self.coche3)
        self.tree.add(self.coche4)
        self.tree.pollFirst()
        self.tree.pollLast()
        self.assertEqual(
            self.tree.size(),
            2,
            "The size of the tree should be 2 after polling the first and last elements.",
        )

    def test_removeCoche(self):
        """
        Tests removing a Coche instance from the TreeSet.

        This test verifies that removing a Coche instance from the TreeSet works correctly.
        """
        self.assertTrue(
            self.tree.add(self.coche), "Adding a Coche instance should return True."
        )
        self.assertFalse(
            self.tree.remove(self.coche),
            "Removing a Coche instance that exists should return False.",
        )

    # The following tests are commented out as they are currently not implemented.
    # def testCeiling(self):
    #     self.assertEqual(self.tree.ceiling("g"), "g")
    #     self.assertEqual(self.tree.ceiling("z"), None)
    #
    # def testFloor(self):
    #     self.assertEqual(self.tree.floor("g"), "g")
    #
    # def testHigher(self):
    #     self.assertEqual(self.tree.higher("g"), "m")
    #
    # def testLower(self):
    #     self.assertEqual(self.tree.lower("g"), "d")

if __name__ == "__main__":
    unittest.main()
