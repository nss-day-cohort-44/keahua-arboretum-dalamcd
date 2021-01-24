from animals import Animal
from animals import Identifiable

class Kikakapu(Animal, Identifiable):

	def __init__(self):
		Animal.__init__(self, "Kikakapu", ["swamp", "river"])
		Identifiable.__init__(self)
		self.__prey = ( "sea anemone", )

	@property
	def prey(self):
		return self.__prey

	def feed(self, prey):
		if prey in self.__prey:
			print(f'The kikakapu ate {prey} for a meal')
		else:
			print(f'The kikakapu rejects the {prey}')

	def __str__(self):
		return f'Kikakapu ({self.id.hex[0:8]}).'
