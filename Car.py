class Car:
    def __init__(self, plate):
        self.plate = plate

    def __eq__(self, plate):
        return self.plate == plate

    def __lt__(self, other):
        return self.plate < other.plate

    def __gt__(self, other):
        return self.plate > other.plate