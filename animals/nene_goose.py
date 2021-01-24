from animals import Animal
from animals import Identifiable

class NeneGoose(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene goose", ["grassland"])
        Identifiable.__init__(self)
        self.__prey = ( "lettuce", "watercress", "bread" )

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Nene goose ate {prey} for a meal.")
        else:
            print(f"The Nene goose rejects the {prey}.")

    def __str__(self):
        return f"{self.species} ({self.id.hex[0:8]})"
