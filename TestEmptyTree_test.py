import unittest

from NullPointerException import NullPointerException
from NoSuchElementException import NoSuchElementException
from TreeSet import TreeSet


class EmptyTree(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(str)

    def testAddNone(self):
        self.assertRaises(NullPointerException, self.tree.add, None)

    def testCelingNonExistingElement(self):
        self.assertEqual(self.tree.ceiling("a"), None)
        
    def testClear(self):
        self.tree.clear()
        self.assertEqual(self.tree.size(), 0)

    def testCloneNonExistingElements(self):
        self.new = self.tree.clone()
        self.assertEqual(self.new.size(), 0)
    
    def testContains(self):
        self.assertFalse(self.tree.contains("a"))

    def testDescendingIterator(self):
        self.iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(self.iterador))
        self.assertEqual(lista, [])
    
    def testFirstNonExistingElement(self):
        self.assertRaises(NoSuchElementException, self.tree.first)
    
    def testFloorNonExistingElement(self):
        self.assertEqual(self.tree.floor("a"), None)
    
    def testHigherNonExistingElement(self):
        self.assertEqual(self.tree.higher("a"), None)
    
    def testIsEmpty(self):
        self.assertTrue(self.tree.isEmpty())

    def testIter(self):
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(iter1))
        self.assertEqual(lista, [])

    def testLastNonExistingElement(self):
        self.assertRaises(NoSuchElementException, self.tree.last)

    def testLowerNonExistingElement(self):
        self.assertEqual(self.tree.lower("a"), None)

    def testPollFirst(self):
        self.assertIsNone(self.tree.pollFirst())
    
    def testPollLast(self):
        self.assertIsNone(self.tree.pollLast())

    def testRemoveNonExistingElement(self):
        self.assertRaises(NullPointerException, self.tree.remove, "a")
        self.assertEqual(self.tree.size(), 0)

    def testSize(self):
        self.assertEqual(self.tree.size(), 0)

if __name__ == "__main__":
    unittest.main()