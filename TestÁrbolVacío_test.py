import unittest

from NullPointerException import NullPointerException
from TreeSet import TreeSet


class EmptyTree(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(str)

    def testSize(self):
        self.assertEqual(self.tree.size(), 0)

    def testContains(self):
        self.assertFalse(self.tree.contains("a"))

    def testAdd(self):
        self.tree.add("a")
        self.assertTrue(self.tree.contains("a"))
        self.assertEqual(self.tree.size(), 1)

    def testAddExistingElement(self):
        self.tree.add("b")
        self.tree.add("b")
        self.assertEqual(self.tree.size(), 1)

    def testRemoveNonExistingElement(self):
        self.assertRaises(NullPointerException, self.tree.remove, "a")
        self.assertEqual(self.tree.size(), 0)

    def testIter(self):
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(iter1))
        self.assertEqual(lista, [])

    # def testPollFirst(self):

    def testClear(self):
        self.tree.clear()
        self.assertEqual(self.tree.size(), 0)

    def testCloneNonExistingElements(self):
        self.tree.clone()
        self.assertEqual(self.tree.size(), 0)

    def testCelingNonExistingElement(self):
        self.assertEqual(self.tree.ceiling("a"), None)


if __name__ == "__main__":
    unittest.main()
