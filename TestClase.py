import unittest
from TreeSet import TreeSet
from Coches import Coches

class TestCoche(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(Coches)
        self.coche = Coches("4578LMZ")

    def test_addCoche(self):
        self.assertTrue(self.tree.add(self.coche))

    # /*def test_removeCoche(self):
    #     self.assertTrue(self.tree.remove(self.coche))

if __name__ == '__main__':
    unittest.main()
