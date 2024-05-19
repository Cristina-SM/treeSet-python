import unittest
from TreeSet import TreeSet
from Coches import Coches
from NullPointerException import NullPointerException

class TestCoche(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(Coches)
        self.coche = Coches("4578LMZ")

    def test_addCoche(self):
        self.assertTrue(self.tree.add(self.coche))
        self.assertFalse(self.tree.remove(self.coche))

    def test_removeCoche(self):
        self.assertTrue(self.tree.add(self.coche))
        self.assertFalse(self.tree.remove(self.coche))

    def testContains(self):
        self.assertFalse(self.tree.contains(Coches("2829abc")))
        self.assertFalse(self.tree.contains(Coches("2384jkl")))
    
    # def testFirst(self):
    #     self.assertEqual(self.tree.first(), "A")
    #
    # def testLast(self):
    #     self.assertEqual(self.tree.last(), "m")
    #
    # def testLower(self):
    #     self.assertEqual(self.tree.lower("g"), "d")
    #
    # def testFloor(self):
    #     self.assertEqual(self.tree.floor("g"), "g")
    #
    # def testHigher(self):
    #     self.assertEqual(self.tree.higher("g"), "m")
    #
    # def testCeiling(self):
    #     self.assertEqual(self.tree.ceiling("g"), "g")
    #     self.assertEqual(self.tree.ceiling("z"), None)
    #
    # def testTreeAfterPoll(self):
    #     self.tree.pollFirst()
    #     self.tree.pollLast()
    #     self.assertEqual(self.tree.__str__(), "['C', 'H', 'a', 'b', 'd', 'g']")
    #     # self.assertRaises()
    #
    def testSize(self):
        self.assertEqual(self.tree.size(), 0)
    
    # def testClone(self):
    #     self.ntree = self.tree.clone()
    #     self.assertEqual(self.ntree.size(), 8)
    #     self.ntree.clear()
    #     self.assertTrue(self.ntree.isEmpty())

    def testNullPointer(self):
        with self.assertRaises(NullPointerException):
            self.tree.add(None)

if __name__ == '__main__':
    unittest.main()