class Coches:
    def __init__(self, matricula):
        self.matricula = matricula

    def __eq__(self, matricula):
        return self.matricula == matricula

    def __lt__(self, matricula2):
        return self.matricula < matricula2