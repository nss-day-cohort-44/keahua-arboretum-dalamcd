from environments import ContainsAnimals, ContainsPlants
from animals import Identifiable

class Forest(ContainsPlants, ContainsAnimals, Identifiable):

	def __init__(self, name):
		ContainsAnimals.__init__(self, 20)
		ContainsPlants.__init__(self, 32)
		Identifiable.__init__(self)
		self.name = name

	def add_animal(self, animal):
		super().add_animal(animal)
	
	def add_plant(self, plant):
		super().add_plant(plant)

	def __str__(self):
		return self.name
