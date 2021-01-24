from animals import Animal
from animals import Identifiable

class Pueo(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo", ["forest", "grassland"])
        Identifiable.__init__(self)
        self.__prey = ( "rat", "mouse", "hampster" )

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Pueo ate {prey} for a meal.")
        else:
            print(f"The Pueo rejects the {prey}.")

    def __str__(self):
        return f"{self.species} ({self.id.hex[0:8]})"
