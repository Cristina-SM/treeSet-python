import unittest

from TreeSet import TreeSet

class NumberTest(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(float)
        self.tree.add(1.2)
        self.tree.add(5.3)
        self.tree.addAll([3.16, 7.0, 7.1, 45.2, 1.3])

    def testAdd(self):
        self.assertFalse(self.tree.add(5.3))
        self.assertFalse(self.tree.addAll([3.16, 7.0, 7.1, 45.2, 1.3]))

    def testCeiling(self):
        self.assertEqual(self.tree.ceiling(3.16), 3.16)
        self.assertEqual(self.tree.ceiling(3.17), 5.3)

    def testClone(self):
        self.ntree = self.tree.clone()
        self.assertEqual(self.ntree.size(), 7)
        self.ntree.clear()
        self.assertTrue(self.ntree.isEmpty())

    def testContains(self):
        self.assertTrue(self.tree.contains(1.2))
        self.assertFalse(self.tree.contains(100.0))

    def testDescendingIterator(self):
        iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iterador))
        self.assertEqual(lista, [45.2, 7.1, 7.0, 5.3, 3.16, 1.3, 1.2])

    def testFirst(self):
        self.assertEqual(self.tree.first(), 1.2)

    def testFloor(self):
        self.assertEqual(self.tree.floor(3.16), 3.16)
        self.assertEqual(self.tree.floor(3.17), 3.16)

    def testHigher(self):
        self.assertEqual(self.tree.higher(3.16), 5.3)

    def testIsEmpty(self):
        self.assertFalse(self.tree.isEmpty())

    def testIter(self):
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iter1))
        self.assertEqual(lista, [1.2, 1.3, 3.16, 5.3, 7.0, 7.1, 45.2])

    def testLast(self):
        self.assertEqual(self.tree.last(), 45.2)

    def testLower(self):
        self.assertEqual(self.tree.lower(3.16), 1.3)

    def testTreeAfterPoll(self):
        self.assertEqual(self.tree.pollFirst(), 1.2)
        self.assertEqual(self.tree.pollLast(), 45.2)
        self.assertEqual(self.tree.__str__(), "['1.3', '3.16', '5.3', '7.0', '7.1']")
        self.assertEqual(self.tree.size(), 5)

    def testRemoveNumber(self):
        self.assertTrue(self.tree.contains(3.16))
        self.tree.remove(3.16)
        self.assertFalse(self.tree.contains(3.16))

    def testSize(self):
        self.assertEqual(self.tree.size(), 7)

if __name__ == "__main__":
    unittest.main()