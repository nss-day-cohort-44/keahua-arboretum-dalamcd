from environments import Biome, ContainsAnimals, ContainsPlants
from animals import Identifiable

class River(Biome, ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name):
        Biome.__init__(self, name, "river")
        ContainsAnimals.__init__(self, 12)
        ContainsPlants.__init__(self, 6)
        Identifiable.__init__(self)