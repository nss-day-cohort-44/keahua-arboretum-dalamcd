from environments import ContainsAnimals, ContainsPlants
from animals import Identifiable
# from animals.


class Swamp(ContainsPlants, ContainsAnimals, Identifiable):

	def __init__(self, name):
		ContainsAnimals.__init__(self)
		ContainsPlants.__init__(self)
		Identifiable.__init__(self)
		self.name = name

	def add_animal(self, animal):
		self.animals.append(animal)

	def __str__(self):
		return self.name
