from animals import Animal
from animals import Identifiable

class HappySpider(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Hawaiian happy face spider", ["swamp"])
        Identifiable.__init__(self)
        self.__prey = ( "fly",)

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Hawaiian happy face spider ate {prey} for a meal.")
        else:
            print(f"The Hawaiian happy face spider rejects the {prey}.")

    def __str__(self):
        return f"{self.species} ({self.id.hex[0:8]})."
