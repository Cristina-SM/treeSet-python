import unittest
from TreeSet import TreeSet

class TestCoche(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet(Coches)
    
    def addCoche(self):
        self.assertTrue(self.tree.add("4578LMZ"))
    


class Coches:
    def __init__(self,matricula, marca):
        self.matricula = matricula
        self.marca = marca

    def __eq__(self, matricula):
        return self.matricula == matricula


    def __lt__(self, matricula):
        return self.matricula < matricula




if __name__ == '__main__':
    unittest.main()

