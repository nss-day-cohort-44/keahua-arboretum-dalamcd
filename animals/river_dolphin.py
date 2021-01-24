from animals import Animal
from animals import Identifiable

class RiverDolphin(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin", ["river", "coastline"])
        Identifiable.__init__(self)
        self.__prey = ( "Trout", "Mackarel", "Salmon", "Sardine" )

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'{self.species} ({self.id.hex[0:8]})'
