from environments import Biome, ContainsAnimals, ContainsPlants
from animals import Identifiable

class Swamp(Biome, ContainsPlants, ContainsAnimals, Identifiable):

    def __init__(self, name):
        Biome.__init__(self, name, "swamp")
        ContainsAnimals.__init__(self, 1)
        ContainsPlants.__init__(self, 12)
        Identifiable.__init__(self)