import unittest
from TreeSet import TreeSet
import NullPointerException

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

    
if __name__ == '__main__':
    unittest.main()