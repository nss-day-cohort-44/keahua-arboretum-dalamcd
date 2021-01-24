from animals import Animal
from animals import Identifiable

class Gecko(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko", ["forest"])
        Identifiable.__init__(self)
        self.__prey = ( "insect", )

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The gold dust day gecko ate {prey} for a meal.")
        else:
            print(f"The gold dust day gecko rejects the {prey}.")

    def __str__(self):
        return f"{self.species} ({self.id.hex[0:8]})."
