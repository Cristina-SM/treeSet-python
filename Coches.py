class Coches:
    def __init__(self,matricula, marca):
        self.matricula = matricula
        self.marca = marca

    def __eq__(self, matricula):
        return self.matricula == matricula

    def __lt__(self, matricula):
        return self.matricula < matricula