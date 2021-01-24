from environments import Biome, ContainsAnimals, ContainsPlants
from animals import Identifiable

class Mountain(Biome, ContainsPlants, ContainsAnimals, Identifiable):

	def __init__(self, name):
		Biome.__init__(self, name, "mountain")
		ContainsAnimals.__init__(self, 6)
		ContainsPlants.__init__(self, 4)
		Identifiable.__init__(self)