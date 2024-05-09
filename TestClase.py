import unittest
from TreeSet import TreeSet
import Coches

class TestCoche(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(Coches)

    def test_addCoche(self):
        self.assertTrue(self.tree.add("4578LMZ"))

    def test_removeCoche(self):
        self.assertTrue(self.tree.remove("4578LMZ"))

if __name__ == '__main__':
    unittest.main()
