import unittest
from TreeSet import TreeSet
from Coches import Coches

class TestCoche(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(Coches)
        self.coche1 = Coches("4578LMZ", "Toyota")
        self.coche2 = Coches("1234ABC", "Ford")
        self.tree.add(self.coche1)

    def test_addCoche(self):
        self.assertTrue(self.tree.add(self.coche2))

    def test_removeCoche(self):
        self.assertTrue(self.tree.remove(self.coche1))


if __name__ == '__main__':
    unittest.main()
