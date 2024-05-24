class Coches:
    def __init__(self, matricula):
        self.matricula = matricula

    def __eq__(self, matricula):
        return self.matricula == matricula

<<<<<<< HEAD
    def __lt__(self, matricula2):
        return self.matricula < matricula2
=======
    def __lt__(self, other):
        return self.matricula < other.matricula

    def __gt__(self, other):
        return self.matricula > other.matricula
>>>>>>> main
