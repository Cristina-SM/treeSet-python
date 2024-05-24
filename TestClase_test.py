import unittest

from Coches import Coches
from NullPointerException import NullPointerException
from TreeSet import TreeSet


class TestCoche(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(Coches)
        self.coche = Coches("4578LMZ")
        self.coche2 = Coches("555ftg")
        self.coche3 = Coches("2829abc")
        self.coche4 = Coches("2384jkl")

    def test_addCoche(self):
        self.assertTrue(self.tree.add(self.coche))
        self.assertFalse(self.tree.remove(self.coche))

    def testClone(self):
        self.tree.add(self.coche2)
        self.tree.add(self.coche3)
        self.ntree = TreeSet(None)
        self.ntree = self.tree.clone()
        self.assertEqual(self.ntree.size(), 2)
        self.ntree.add(self.coche4)
        self.assertEqual(self.ntree.size(), 3)
        self.ntree.clear()
        self.assertTrue(self.ntree.isEmpty())

    def testContains(self):
        self.assertFalse(self.tree.contains(Coches("2829abc")))
        self.assertFalse(self.tree.contains(Coches("2384jkl")))

    def testFirst(self):
        self.tree.add(self.coche)
        self.assertEqual(self.tree.first(), "4578LMZ")

    def testLast(self):
        self.tree.add(self.coche)
        self.tree.add(self.coche2)
        self.assertEqual(self.tree.last(), "555ftg")

    def testNullPointer(self):
        with self.assertRaises(NullPointerException):
            self.tree.add(None)
        with self.assertRaises(NullPointerException):
            self.tree.remove("6952rtr")

    def testSize(self):
        self.assertEqual(self.tree.size(), 0)

    def testTreeAfterPoll(self):
        self.tree.add(self.coche)
        self.tree.add(self.coche2)
        self.tree.add(self.coche3)
        self.tree.add(self.coche4)
        self.tree.pollFirst()
        self.tree.pollLast()
        self.assertEqual(self.tree.size(), 2)

    def test_removeCoche(self):
        self.assertTrue(self.tree.add(self.coche))
        self.assertFalse(self.tree.remove(self.coche))

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