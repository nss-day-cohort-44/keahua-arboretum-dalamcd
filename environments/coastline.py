from environments import Biome, ContainsAnimals, ContainsPlants
from animals import Identifiable

class Coastline(Biome, ContainsPlants, ContainsAnimals, Identifiable):

	def __init__(self, name):
		Biome.__init__(self, name, "coastline")
		ContainsAnimals.__init__(self, 22)
		ContainsPlants.__init__(self, 15)
		Identifiable.__init__(self)
