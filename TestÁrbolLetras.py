import unittest
from TreeSet import TreeSet

class LetterTest(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet()
        self.tree.add("b")
        self.tree.add("a")
        self.tree.add("d")
        self.tree.add("g")
        self.tree.add("m")

    def testContains(self):
        self.assertTrue(self.tree.contains("b"))
        self.assertFalse(self.tree.contains("z"))

    def removeLetter(self):
        self.assertTrue(self.tree.contains("a"))
        self.tree.remove("a")
        self.assertFalse(self.tree.contains("a"))

    def testFirst(self):
        self.assertEqual(self.tree.first(), "a")
    
    def testLast(self):
        self.assertEqual(self.tree.last(), "m")
    
    def testLower(self):
        self.assertEqual(self.tree.lower("b"), "a")

    def testFloor(self):
        self.assertEqual(self.tree.floor("c"), "b")

    def testHigher(self):
        self.assertEqual(self.tree.higher("d"), "g")

    def testIter(self):
        iter1 = self.tree.__iter__()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(iter1))   
        self.assertEqual(lista, ['a', 'b', 'd', 'g', 'm'])

    
if __name__ == '__main__':
    unittest.main()
