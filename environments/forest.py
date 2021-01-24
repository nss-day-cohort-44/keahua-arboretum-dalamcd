from environments import Biome, ContainsAnimals, ContainsPlants
from animals import Identifiable

class Forest(Biome, ContainsPlants, ContainsAnimals, Identifiable):

	def __init__(self, name):
		Biome.__init__(self, name, "forest")
		ContainsAnimals.__init__(self, 20)
		ContainsPlants.__init__(self, 32)
		Identifiable.__init__(self)


