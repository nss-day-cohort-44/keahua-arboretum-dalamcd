class Biome():

	def __init__(self, name, biome_type):
		self.name = name
		self.biome_type = biome_type

	def check_suitability(self, thing):
		for b in thing.biome_types:
			if self.biome_type == b:
				return True
		return False

	def __str__(self):
		return self.name