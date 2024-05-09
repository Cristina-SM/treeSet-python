import unittest
from TreeSet import TreeSet
from Coches import Coches

class TestCoche(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(Coches)
        self.coche1 = Coches("4578LMZ")
        self.coche2 = Coches("9858PTD")
        self.tree.add(self.coche1)

    def test_addCoche(self):
        self.assertFalse(self.tree.add(self.coche1))
        self.assertTrue(self.tree.add(self.coche2))


    def test_removeCoche(self):
        self.assertTrue(self.tree.remove(self.coche1))
    
    def test_lenCoche(self):
        self.assertEqual(self.tree.size(),1)
    
    def test_comparaMatricula1(self):
        self.assertTrue(self.coche1.matricula.__eq__("4578LMZ"))

    def test_comparaMatricula2(self):
        self.assertFalse(self.coche1.matricula.__eq__(self.coche2.matricula))


if __name__ == '__main__':
    unittest.main()
