from animals import Animal
from animals import Identifiable

class Ulae(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "'Ulae", ["coastline"])
        Identifiable.__init__(self)
        self.__prey = ( "small fish", )

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The 'ulae ate {prey} for a meal")
        else:
            print(f"The 'ulae rejects the {prey}")

    def __str__(self):
        return f"'Ulae ({self.id.hex[0:8]})."
