from animals import Animal
from animals import Identifiable

class OpeApeA(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a", ["forest", "mountain"])
        Identifiable.__init__(self)
        self.__prey = ( "grass", "fly" )

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Ope'ape'a ate {prey} for a meal.")
        else:
            print(f"The Ope'ape'a rejects the {prey}.")

    def __str__(self):
        return f"Ope'ape'a ({self.id.hex[0:8]})."
