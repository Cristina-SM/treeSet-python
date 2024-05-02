import unittest
from TreeSet import TreeSet

class LetterTest(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet()
        self.tree.add("b")
        self.tree.add("A")
        self.tree.add("d")
        self.tree.add("g")
        self.tree.add("m")
        self.tree.add("H")
        self.tree.add("a")
        self.tree.add("C")
    
    def testContains(self):
        self.assertTrue(self.tree.contains("b"))
        self.assertFalse(self.tree.contains("z"))
    
    def removeLetter(self):
        self.assertTrue(self.tree.contains("a"))
        self.tree.remove("a")
        self.assertFalse(self.tree.contains("a"))
    
    def testFirst(self):
        self.assertEqual(self.tree.first(), "A")
    
    def testLast(self):
        self.assertEqual(self.tree.last(), "m")
    
    def testLower(self):
        self.assertEqual(self.tree.lower("g"), "d")
    
    def testFloor(self):
        self.assertEqual(self.tree.floor("g"), "g")

    def testHigher(self):
        self.assertEqual(self.tree.higher("g"), "m")
    
    def testCeiling(self):
        self.assertEqual(self.tree.ceiling("g"), "g")
        self.assertEqual(self.tree.ceiling("z"), None)
    
    def testTreeAfterPoll(self):
        self.tree.pollFirst()
        self.tree.pollLast()
        self.assertEqual(self.tree.__str__(), "['C', 'H', 'a', 'b', 'd', 'g']")
        #self.assertRaises()
    
    def testSize(self):
        self.assertEqual(self.tree.size(), 8)
    
    def testClone(self):
        self.ntree = self.tree.clone()
        self.assertEqual(self.ntree.size(), 8)
        self.ntree.clear()
        self.assertTrue(self.ntree.isEmpty())
    
    def testIsEmpty(self):
        self.assertFalse(self.tree.isEmpty())
    
    def testDescendingIterator(self):
        self.iterador = self.tree.descendingIterator()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(self.iterador))
        self.assertEqual(lista, ['m', 'g', 'd', 'b', 'a', 'H', 'C', 'A'])   
    
    def testIter(self):
        self.iterador = self.tree.__iter__()
        lista = []
        for _ in range(0, self.tree.size()):
            lista.append(next(self.iterador))
        self.assertEqual(lista, ['A', 'C', 'H', 'a', 'b', 'd', 'g', 'm'])

    def testClearClone(self):
        self.new = self.tree.clone()
        self.new.clear()
        self.assertTrue(self.new.isEmpty())
        self.assertFalse(self.tree.isEmpty())
    
if __name__ == '__main__':
    unittest.main()
