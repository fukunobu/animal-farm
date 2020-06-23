""" A leopard """
import animal

class Leopard(animal.Animal):
    def __init__(self):
        self.kind = 'Leopard'
    def get_kind(self):
        return self.kind
