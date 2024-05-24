import unittest

from TreeSet import TreeSet

class NumberTest(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(int)
        self.tree.add(1)
        self.tree.add(53)
        self.tree.addAll([36, 70, 7, 45, 11])

    def testAdd(self):
        self.assertFalse(self.tree.add(53))
        self.assertFalse(self.tree.addAll([36, 70, 7, 45, 11]))

    def testCeiling(self):
        self.assertEqual(self.tree.ceiling(36), 36)
        self.assertEqual(self.tree.ceiling(37), 45)

    def testClone(self):
        self.ntree = self.tree.clone()
        self.assertEqual(self.ntree.size(), 7)
        self.ntree.clear()
        self.assertTrue(self.ntree.isEmpty())

    def testContains(self):
        self.assertTrue(self.tree.contains(1))
        self.assertFalse(self.tree.contains(100))

    def testDescendingIterator(self):
        iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iterador))
        self.assertEqual(lista, [70, 53, 45, 36, 11, 7, 1])

    def testFirst(self):
        self.assertEqual(self.tree.first(), 1)

    def testFloor(self):
        self.assertEqual(self.tree.floor(36), 36)
        self.assertEqual(self.tree.floor(37), 36)

    def testHigher(self):
        self.assertEqual(self.tree.higher(36), 45)

    def testIsEmpty(self):
        self.assertFalse(self.tree.isEmpty())

    def testIter(self):
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(self.tree.size()):
            lista.append(next(iter1))
        self.assertEqual(lista, [1, 7, 11, 36, 45, 53, 70])

    def testLast(self):
        self.assertEqual(self.tree.last(), 70)

    def testLower(self):
        self.assertEqual(self.tree.lower(29), 11)

    def testTreeAfterPoll(self):
        self.assertEqual(self.tree.pollFirst(), 1)
        self.assertEqual(self.tree.pollLast(), 70)
        self.assertEqual(self.tree.__str__(), "['7', '11', '36', '45', '53']")
        self.assertEqual(self.tree.size(), 5)

    def testRemoveNumber(self):
        self.assertTrue(self.tree.contains(36))
        self.tree.remove(36)
        self.assertFalse(self.tree.contains(36))

    def testSize(self):
        self.assertEqual(self.tree.size(), 7)

if __name__ == "__main__":
    unittest.main()